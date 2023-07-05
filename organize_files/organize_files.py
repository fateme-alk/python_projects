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

def copy_file(src_file_path, dst_file_path):
    open(dst_file_path, "w")
    with open(src_file_path, 'rb') as src_file:
        with open(dst_file_path, 'wb') as dest_file:
            dest_file.write(src_file.read())

categories = {
    'pic': ('jpg', 'jpeg', 'png'),
    'video': ('mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov'),
    'compressed': ('zip', 'rar'),
    'internet_related': ('html', 'css', 'js'),
    'text': ('doc', 'docs', 'txt', 'pdf'),
    'database': ('sqlite', 'sqlite3', 'db3', 'db', 'dbf', 'sql'),
}   

_, src_folder_path, dst_folder_path = tuple(sys.argv)

for dir_path, dir_names, file_names in os.walk(src_folder_path):
    for file_name in file_names:
        src_file_path = os.path.join(dir_path, file_name)
        file_year = str(modification_date(src_file_path).tm_year)
        create_dir(dst_folder_path, file_year)
        file_extension = find_file_extension(file_name)
        for category, extensions_of_category in categories.items():
            if file_extension in extensions_of_category:
                create_dir(os.path.join(dst_folder_path, file_year),category)
                dst_file_path = os.path.join(dst_folder_path, file_year, category, file_name)
                copy_file(src_file_path, dst_file_path)
            