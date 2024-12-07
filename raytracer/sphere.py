import math

from vector import Vec3

# Définition d'une sphère
class Sphere:
    def __init__(self, center, radius, color, reflectivity, transparency):
        self.center = center
        self.radius = radius
        self.color = color
        self.reflectivity = reflectivity
        self.transparency = transparency

    def intersect(self, ray_origin, ray_direction):
        oc = Vec3(ray_origin.x - self.center.x,
                  ray_origin.y - self.center.y,
                  ray_origin.z - self.center.z)

        a = ray_direction.dot(ray_direction)
        b = 2.0 * oc.dot(ray_direction)
        c = oc.dot(oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return -1
        else:
            t1 = (-b - math.sqrt(discriminant)) / (2.0 * a)
            t2 = (-b + math.sqrt(discriminant)) / (2.0 * a)
            return min(t1, t2)

    def normal(self, surface_point):
        return (surface_point - self.center).normalize()