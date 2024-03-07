import os
import shutil
from datetime import datetime

from PIL import Image

extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.psd', '.cr2', '.dng', '.raw']


def folder_path(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')


def photo_shooting_date(file):
    img = Image.open(file)
    info = img.getexif()
    if 36867 in info:
        date = info[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date


def move_file(file):
    new_folder = folder_path(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    shutil.move(file, new_folder + '/' + file)


def organize_files(self):
    photo = [filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in extensions)]
    for filename in photo:
        self.move_file(filename)


print(move_file('yellow-lab.jpeg'))
