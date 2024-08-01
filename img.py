import csv
from PIL import Image

with open('pixel_values.csv', 'r') as file:
    reader = csv.reader(file)
    pixel_data = list(reader)

pixel_data = [int(pixel) for row in pixel_data for pixel in row]

width, height = 52, 7
image = Image.new('1', (width, height))

for y in range(height):
    for x in range(width):
        pixel_value = pixel_data[y * width + x]
        image.putpixel((x, y), pixel_value)

image.save('output_image.png')
image.show()
