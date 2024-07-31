import tkinter as tk
from PIL import Image, ImageDraw
import csv

grid_width = 52
grid_height = 7
block_size = 20

image_width = grid_width * block_size
image_height = grid_height * block_size
image = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

root = tk.Tk()
root.title("Pixel Drawing")

canvas = tk.Canvas(root, width=image_width, height=image_height, bg='white')
canvas.pack()

for x in range(0, image_width, block_size):
    for y in range(0, image_height, block_size):
        canvas.create_rectangle(x, y, x + block_size, y + block_size, outline='gray')

def draw_pixel(event):
    x = (event.x // block_size) * block_size
    y = (event.y // block_size) * block_size
    canvas.create_rectangle(x, y, x + block_size, y + block_size, fill='black', outline='gray')
    draw.rectangle([x, y, x + block_size, y + block_size], fill='black')

canvas.bind("<B1-Motion>", draw_pixel)
canvas.bind("<Button-1>", draw_pixel)

def save_image():
    image.save('pixelated_drawing.png')
    save_csv()

def save_csv():
    pixel_values = []
    for y in range(0, image_height, block_size):
        row = []
        for x in range(0, image_width, block_size):
            pixel = image.getpixel((x + block_size // 2, y + block_size // 2))
            if pixel == (0, 0, 0):
                row.append(1)
            else:
                row.append(0)
        pixel_values.append(row)
    
    with open('pixel_values.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(pixel_values)

save_button = tk.Button(root, text="Save", command=save_image)
save_button.pack()

root.mainloop()
