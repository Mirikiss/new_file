# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
import pathlib
import shutil

def  sort_files(source_folder):
    video_extensions = ['.mp4', '.avi', '.move']
    image_extensions = ['.jpg', '.png', '.gif']
    text_extensions = ['.txt', '.doc', '.pdf']

    for file in os.listdir(source_folder):
        filname, extension = os.path.splitext(file)

        if extension.lower() in video_extensions:
            destination_folder = 'Видео'
        elif extension.lower() in image_extensions:
            destination_folder = 'Изображение'
        elif extension.lower() in text_extensions:
            destination_folder = 'Текст'
        else:
            continue

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(source_folder, destination_folder, file)
        shutil.move(source_path, destination_path)
    remaining_files = [file for file in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, file))]
    return remaining_files
source_folder = 'путь к фалу'
fail_1 = sort_files(source_folder)
print(fail_1)