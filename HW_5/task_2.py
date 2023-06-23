# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os


def split_path(file_path):
    file_name = os.path.basename(file_path)
    path = os.path.dirname(file_path)
    name, extension = os.path.splitext(file_name)
    return (path, name, extension)


#file_path = '/home/user/Desktop/my_file.txt'
#path, name, extension = split_path(file_path)
#print(path)  # /home/user/Desktop
#print(name)  # my_file
#print(extension)  # .txt
