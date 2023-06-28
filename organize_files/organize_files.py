import sys
import os
import time

def modification_date(file_path):
    file_date = time.strptime(time.ctime(os.path.getmtime(file_path)))
    return file_date

def create_dir(parent_dir, dir_name):
    path = os.path.join(parent_dir ,dir_name)
    if not(os.path.isdir(path)):
        os.mkdir(path)

def find_file_extension(file_name):
    return (file_name.split('.')[-1]).lower()

categories = {
    'pic': ('jpg', 'jpeg', 'png'),
    'video': ('mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov'),
}   

_, src_folder_path, dst_folder_path = tuple(sys.argv)

for dir_path, dir_names, file_names in os.walk(src_folder_path):
    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        file_year = str(modification_date(file_path).tm_year)
        create_dir(dst_folder_path, file_year)
        