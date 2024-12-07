import math

from vector import Vec3
from sphere import Sphere
from camera import Camera
from utils import generate_ppm, width, height
from benchmark import benchmark_profile, benchmark_time

# Fonction de rendu des sphères
def render(camera, spheres):
    aspect_ratio = width / height
    image_data = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            # Convertir les coordonnées de l'écran en coordonnées de l'espace de la caméra
            ndc_x = (2 * (x + 0.5) / width - 1) * math.tan(camera.fov / 2) * aspect_ratio
            ndc_y = (1 - 2 * (y + 0.5) / height) * math.tan(camera.fov / 2)

            # Calculer la direction du rayon pour le pixel actuel
            ray_direction = (camera.right * ndc_x + camera.up * ndc_y + camera.direction).normalize()

            # Intersection du rayon avec les sphères
            closest_sphere = None
            closest_t = float('inf')

            for sphere in spheres:
                t = sphere.intersect(camera.position, ray_direction)
                if 0 < t < closest_t:
                    closest_t = t
                    closest_sphere = sphere

            # Calcul de la couleur du pixel
            if closest_sphere:
                intersection_point = camera.position + ray_direction * closest_t
                normal = (intersection_point - closest_sphere.center).normalize()
                color = closest_sphere.color
                intensity = max(0, normal.dot(Vec3(0, 0, 0) - ray_direction))
                final_color = (int(color[0] * intensity), int(color[1] * intensity), int(color[2] * intensity))
                image_data[y][x] = final_color

    generate_ppm(image_data)


# Fonction main avec un exemple de caméra pour render une boule rouge et une boule blanche
def main():
    camera = Camera(Vec3(0, 0, 0), Vec3(0, 0, -1), Vec3(0, 1, 0), 60)

    sphere1 = Sphere(Vec3(1, 0, -3), 0.5, (255, 255, 255))
    sphere2 = Sphere(Vec3(-1, 0, -3), 0.5, (255, 0, 0))

    spheres = [sphere1, sphere2]

    render(camera, spheres)


main()
