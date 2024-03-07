import os
from datetime import datetime

from PIL import Image


def photo_shooting_date(file):
    img = Image.open(file)
    info = img.getexif()
    if 36867 in info:
        date = info[36867]
        date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    else:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date


print(photo_shooting_date('test.jpg'))
