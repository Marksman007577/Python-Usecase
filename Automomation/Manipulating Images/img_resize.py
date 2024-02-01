from PIL import Image
Img = Image.open('house.png')
width, height = Img.size
quartersizedImg = Img.resize((int(width / 2), int(height / 2)))
quartersizedImg.save('quartersized.jpg')
