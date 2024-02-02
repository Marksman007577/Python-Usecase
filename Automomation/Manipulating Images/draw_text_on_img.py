from PIL import Image, ImageColor, ImageDraw, ImageFont
import os
img = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(img)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
img.save('text.png')
