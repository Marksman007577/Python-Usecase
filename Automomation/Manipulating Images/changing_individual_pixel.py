from PIL import Image, ImageColor

img = Image.new(mode='RGBA', size=(500, 600))

for x in range(100):
    for y in range(50):
        img.putpixel((x,y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        img.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

img.save('put_pixel.png')
