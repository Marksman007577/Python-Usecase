from PIL import Image
Img = Image.open('house.png')
Img.rotate(270, expand=True).save('house_rotated.png')
