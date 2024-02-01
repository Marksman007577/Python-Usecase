from PIL import Image

img = Image.open('house.jpg')
cropped_img = img.crop((335, 345, 505, 560))
cropped_img.save('cropped_house.jpg')
cropped_img.show()