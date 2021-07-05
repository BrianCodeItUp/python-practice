from sys import argv
from os import *
from PIL import Image

# grab first and second arguments
image_folder = argv[1]
output_folder = argv[2]

# create folder to put converted images
if not path.exists(output_folder):
    mkdir(output_folder)
    print("Directory " , output_folder ,  " Created ")

for filename in listdir(image_folder):
  with Image.open(f'{image_folder}{filename}') as img:
    clean_name = path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'Save {output_folder}{clean_name}.png successfully')