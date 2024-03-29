import os
import shutil
from datetime import datetime

from PIL import Image


class PhotoSort:
    DATETIME_EXIF_INFO_ID = 36867
    extensions = ['jpg', 'jpeg', 'png', 'bmp', 'tif',
                  'tiff', 'psd', 'cr2', 'dng', 'raw']

    def folder_path(self, file):
        date = self.photo_shooting_date(file)
        return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

    def photo_shooting_date(self, file):
        date = None
        img = Image.open(file)
        if hasattr(img, '_getexif'):
            info = img._getexif()
            if info:
                if self.DATETIME_EXIF_INFO_ID in info:
                    date = info[self.DATETIME_EXIF_INFO_ID]
                    date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        if date is None:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def move_file(self, file):
        new_folder = self.folder_path(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def organize_files(self):
        photo = [filename for filename in os.listdir('.')
                 if os.path.isfile(filename) and any(filename.lower().endswith('.' + ext.lower())
                                                     for ext in self.extensions)]
        for filename in photo:
            self.move_file(filename)


PS = PhotoSort()
PS.organize_files()
