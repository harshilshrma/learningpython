from PIL import Image

image_path = 'C:/Users/harsh/PycharmProjects/LearningPython/DMW Lab Sem-V/sakuta.jpg'
image = Image.open(image_path)

width, height = image.size

print(f"Image resolution: {width}x{height}")
print(f"Image format: {image.format}")
