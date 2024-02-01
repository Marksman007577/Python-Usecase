from PIL import Image
Img = Image.open('house.png')
Img.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip_house.jpg')
Img.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip_house.jpg')
