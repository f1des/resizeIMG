from PIL import Image

import os

def resize_images(folder_path, width, height):
  for file_name in os.listdir(folder_path):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):
      file_path = os.path.join(folder_path, file_name)
      image = Image.open(file_path)
      image = image.resize((width, height))
      new_file_name = 'resize_' + file_name

      new_file_path = os.path.join(folder_path, new_file_name)
      image.save(new_file_path)

resize_images('C:\\Users\\adminchi\\Desktop\\download_site', 456, 304)