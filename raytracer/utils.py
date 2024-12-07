width = 800
height = 600

# Fonction de génération de fichier .ppm
def generate_ppm(image_data):
    file = open("image.ppm", "w")

    ppm_header = f"P3\n{width} {height}\n255\n"
    ppm_data = ""

    for row in image_data:
        for pixel in row:
            ppm_data += f"{pixel[0]} {pixel[1]} {pixel[2]} "
        ppm_data += "\n"

    ppm_data = ppm_header + ppm_data

    file.write(ppm_data)

    file.close()