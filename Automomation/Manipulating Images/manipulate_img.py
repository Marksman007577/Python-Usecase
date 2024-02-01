from PIL import Image

# read image file
img = Image.open('house.jpg')


# check image dimensions
img_dim = img.size
img_width, img_height = img.size
print(img_width, img_height)

# checking the image format
img_format = img.format
img_format_desc = img.format_description
print(img_format, img_format_desc)

# save an image
img.save('house.png', 'png')