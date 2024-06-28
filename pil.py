from PIL import Image, ImageFilter

# Open Image
img = Image.open('gambar.png')

print(f"format : {img.format}, ukuran:{img.size}, Mode:{img.mode}")

resized_image = img.resize((300,200))
resized_image.save('example_resized.png')
print(f"format : {resized_image.format}, ukuran:{resized_image.size}, Mode:{resized_image.mode}")

img.save('example_image.png')

blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save('example_blurred.png')

img.close()