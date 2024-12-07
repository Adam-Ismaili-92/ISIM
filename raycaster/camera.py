import math

# Définition d'une caméra
class Camera:
    def __init__(self, position, target, up, fov):
        self.position = position
        self.direction = (target - position).normalize()
        self.right = up.cross(self.direction).normalize()
        self.up = self.direction.cross(self.right).normalize()
        self.fov = math.radians(fov)