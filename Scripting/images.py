from PIL import Image, ImageFilter

img = Image.open('./pokedex/208_astro.jpg')
# new_img=img.resize((400,200))
img.thumbnail((400, 400))
# new_img.save('thumbnail.jpg')
img.save('thumbnail.jpg')
print(img.size)

# filtered_image = img.filter(ImageFilter.BLUR)
# filtered_image = img.filter(ImageFilter.SMOOTH)
# filtered_image = img.filter(ImageFilter.SHARPEN)
# filtered_image = img.convert('L')
# box = (100,100,400,400)

# crooked = filtered_image.rotate(90)
# resize = filtered_image.resize((300,300))
# region = filtered_image.crop(box)
# filtered_image.save("blur.png","png")

# region.save("grey.png", "png")

# filtered_image.show()
