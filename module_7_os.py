import os
import time

cur_dir = os.getcwd()

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(cur_dir, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
