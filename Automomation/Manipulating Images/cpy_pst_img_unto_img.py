from PIL import Image
Im = Image.open('house.png')
Im_copy = Im.copy()

new_Im = Im.crop((335, 345, 565, 560))
Im_copy.paste(new_Im, (0, 0))
Im_copy.paste(new_Im, (400, 500))
Im_copy.save('paste.png', 'png')
