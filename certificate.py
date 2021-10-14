from PIL import Image, ImageDraw, ImageFont
 
name =input("Enter Your name")

im = Image.open('new.jpg')
d = ImageDraw.Draw(im)
location = (25, 220)
text_color = (0, 137, 209)
font = ImageFont.truetype("arial.ttf", 80)
d.text(location,name,  fill = text_color, font = font)

im.save("certificate"+".jpg")
im.show()