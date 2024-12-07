import math

# Définition d'une classe de vecteur3
class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Addition de vecteur3
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    # Soustraction de vecteur3
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    # Multiplication de vecteur3 et de scalaire
    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    # Division de vecteur3 et de scalaire
    def __truediv__(self, scalar):
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    # Longueur euclidienne du vecteur3
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    # Normalisation du vecteur3
    def normalize(self):
        length = self.length()
        if length != 0:
            self.x /= length
            self.y /= length
            self.z /= length
        return self

    # Produit scalaire avec un autre vecteur3
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Produit vectoriel avec un autre vecteur3
    def cross(self, other):
        return Vec3(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)