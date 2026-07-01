from PIL import Image as Pillow
image = r"C:\Users\user\Downloads\star.png" # your image path here
image = Pillow.open(image).convert("RGBA")
width, height = image.size
pixels = image.load()

def tohex(num):
    return format(num, '02x')

res = ""
for x in range(width):
    for y in range(height):
        res = res + str(y * width + x + 1) + ":" + tohex(pixels[x,y][0]) + tohex(pixels[x,y][1]) + tohex(pixels[x,y][2]) + ","
print(res)
