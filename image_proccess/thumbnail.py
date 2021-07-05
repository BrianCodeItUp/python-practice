from PIL import Image, ImageFilter

astro_img = Image.open('./images/astro.jpeg')
astro_img.thumbnail((400, 400))
astro_img.save('thumb.jpg')

