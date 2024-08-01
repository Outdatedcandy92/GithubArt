from PIL import Image

pixel_data = [stuff]
pixel_data = [int(pixel) for pixel in pixel_data]
pixel_data = [1 if pixel == 1 else 0 for pixel in pixel_data]

width, height = 52, 7

image = Image.new('1', (width, height))
image.putdata(pixel_data)
image.save('output_image.png')
image.show()
