# Définition d'un Triangle
class Triangle:
    def __init__(self, a, b, c, color, reflectivity, transparency):
        self.a = a
        self.b = b
        self.c = c
        self.color = color
        self.reflectivity = reflectivity
        self.transparency = transparency

    def intersect(self, ray_origin, ray_direction):
        edge1 = self.b - self.a
        edge2 = self.c - self.a
        h = ray_direction.cross(edge2)
        a = edge1.dot(h)

        if -0.00001 < a < 0.00001:
            return -1

        f = 1.0 / a
        s = ray_origin - self.a
        u = f * s.dot(h)

        if u < 0.0 or u > 1.0:
            return -1

        q = s.cross(edge1)
        v = f * ray_direction.dot(q)

        if v < 0.0 or u + v > 1.0:
            return -1

        t = f * edge2.dot(q)

        if t > 0.00001:
            return t
        else:
            return -1
        
        def normal(self, surface_point):
            return (self.b - self.a).cross(self.c - self.a).normalize()