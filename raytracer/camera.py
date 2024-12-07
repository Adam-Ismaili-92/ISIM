import math

# Définition d'une caméra
class Camera:
    def __init__(self, position, target, up, fov):
        self.position = position
        self.direction = (target - position).normalize()
        self.right = up.cross(self.direction).normalize()
        self.up = self.direction.cross(self.right).normalize()
        self.fov = math.radians(fov)
        
# Fonction permettant le calcul de la direction du rayon pour chaque pixel
def calculate_ray_direction(pixel_x, pixel_y, image_width, image_height, camera):
    aspect_ratio = image_width / image_height

    fov_tan = math.tan(camera.fov / 2)
    normalized_x = (2 * ((pixel_x + 0.5) / image_width) - 1) * aspect_ratio
    normalized_y = (2 * ((pixel_y + 0.5) / image_height) - 1) * aspect_ratio

    camera_right = camera.right * fov_tan * aspect_ratio * normalized_x
    camera_up = camera.up * fov_tan * normalized_y
    camera_direction = camera.direction + camera_right + camera_up

    return camera_direction