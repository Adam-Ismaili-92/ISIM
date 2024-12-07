# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:58:52 2023

@author: dokli
"""

import math

from vector import Vec3
from sphere import Sphere
from triangle import Triangle
from camera import Camera, calculate_ray_direction
from utils import generate_ppm, width, height
from benchmark import benchmark_profile, benchmark_time


# Fonction pour lancer un rayon et calculer la couleur du pixel
def cast_ray(ray_origin, ray_direction, objects, light_sources, depth=0):
    if depth > 3:
        return 0, 0, 0  # Limite de réflexion atteinte, retourne la couleur noire

    # Recherche de l'intersection la plus proche
    closest_intersection = math.inf
    closest_obj = None
    for obj in objects:
        intersection = obj.intersect(ray_origin, ray_direction)
        if 0 < intersection < closest_intersection:
            closest_intersection = intersection
            closest_obj = obj

    if closest_obj is None:
        # Dégradé de couleur pour le fond
        start_color = (255, 213, 128)  # Couleur de départ (bleu)
        end_color = (201, 126, 253)  # Couleur de fin (violet clair)

        # Calcul de la couleur du pixel en fonction de sa direction
        background_color = (
            int(start_color[0] + (end_color[0] - start_color[0]) * (ray_direction.y * 0.5 + 0.5)),
            int(start_color[1] + (end_color[1] - start_color[1]) * (ray_direction.y * 0.5 + 0.5)),
            int(start_color[2] + (end_color[2] - start_color[2]) * (ray_direction.y * 0.5 + 0.5))
        )

        return background_color
        # return (201,126,253)  # Pas d'intersection, retourne la couleur violet claire

    # Calcul de la position de l'intersection
    intersection_point = ray_origin + ray_direction * closest_intersection

    # Calcul de la normale à la objet à l'intersection
    normal = closest_obj.normal(intersection_point)

    # Calcul de la direction du rayon réfléchi
    reflected_direction = ray_direction - normal * 2.0 * ray_direction.dot(normal)

    # Vérifie si le rayon réfléchi intersecte une autre objet
    reflection_color = cast_ray(intersection_point, reflected_direction, objects, light_sources, depth + 1)

    # Calcul de l'éclairage
    light_intensity = 0
    for light_source in light_sources:
        light_direction = (light_source - intersection_point).normalize()

        light_intensity_local = max(0, light_direction.dot(normal))
        if light_intensity_local != 0:
            # is the point in shadow?
            shadow_origin = intersection_point + normal * 1e-3
            shadow_intersection = math.inf
            for obj in objects:
                intersection = obj.intersect(shadow_origin, light_direction)
                if 0 < intersection < shadow_intersection:
                    shadow_intersection = intersection
                    break
            if shadow_intersection < math.inf:
                light_intensity_local = 0
        light_intensity += light_intensity_local

    # Eclairage ambiant
    ambient_color = (30, 30, 30)

    # Calcul de la couleur finale
    sphere_color = closest_obj.color
    color = (
        int(sphere_color[0] * light_intensity),
        int(sphere_color[1] * light_intensity),
        int(sphere_color[2] * light_intensity)
    )

    # Blend the reflection color, refraction color, and object color
    transparency = closest_obj.transparency
    color = (
        int(color[0] * (1 - transparency) + reflection_color[0] * transparency),
        int(color[1] * (1 - transparency) + reflection_color[1] * transparency),
        int(color[2] * (1 - transparency) + reflection_color[2] * transparency)
    )

    # Ajout de l'éclairage ambiant à la couleur finale
    color = (
        min(color[0] + ambient_color[0], 255),
        min(color[1] + ambient_color[1], 255),
        min(color[2] + ambient_color[2], 255)
    )

    return color


# Fonction de rendu de objets généré par raytracing, ne prend qu'une seule source de lumière
def render(camera, objects, light):
    image_data = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if x == 196 and y == 218:
                print(f"Rendering pixel {x}, {y}")

            ray_direction = calculate_ray_direction(x, y, width, height, camera)
            ray_direction.normalize()

            color = cast_ray(camera.position, ray_direction, objects, light)
            image_data[y][x] = color

    generate_ppm(image_data)


# Fonction main avec un exemple de caméra pour render une boule rouge et une boule blanche
def main():
    camera = Camera(Vec3(0, 0, 0), Vec3(0, 0, -1), Vec3(0, 1, 0), 60)

    sphere1 = Sphere(Vec3(0, 0.2, -2), 0.2, (255, 255, 255), 0.5, 0.8)
    sphere2 = Sphere(Vec3(0, -1.2, -2), 0.9, (255, 255, 255), 0.5, 0.8)

    #triangle1 = Triangle(Vec3(-0.3, 0.2, -1), Vec3(0.3, 0.2, -1), Vec3(0, 0, -2), (255, 255, 255), 0.5)

    spheres = [sphere1, sphere2]

    #light1 = Vec3(-0.2, 1, -2)
    #light2 = Vec3(0.2, 1, -2)
    light3 = Vec3(0, 1, -2)

    lights = [light3]

    render(camera, spheres, lights)


main()
