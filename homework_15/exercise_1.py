# 📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: ○ имя файла без расширения или название каталога, ○ расширение, если это файл, ○ флаг каталога, ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
import argparse
import os
import logging

# парсер
parser = argparse.ArgumentParser()
parser.add_argument("path", help="Путь к файлу или директории", type=str)
args = parser.parse_args()
# print(args.path)


# логгер
logger = logging.getLogger(__name__)

format = "{asctime:<20} - {levelname:<10} -{msg}"
logging.basicConfig(
    filename="mylog_home.log",
    filemode="w",
    encoding="UTF-8",
    level=logging.INFO,
    style="{",
    format=format,
)


def get_file(path: str = os.getcwd()):
    file_list = []
    size_f = 0
    for obj in os.listdir(path):  # обходит все папки, подпапки, файлы
        objpath = os.path.join(obj) 
        parts = path.split(os.sep, maxsplit=1)
        parent_dir = os.path.splitdrive(path)[1]
        parent_dir = parent_dir.split("\\")[-1]

        if os.path.isfile(objpath):
            objpath = os.path.splitext(obj)
            file_list.append(f"{objpath[0]}, {objpath[1]}, False, {parent_dir}")
        elif os.path.isdir(objpath):
            file_list.append(f"{objpath}, без расширения, True, {parent_dir}")
    return file_list


lst = get_file(args.path)

Direct = namedtuple("Direct", ["file_dir_name", "expansion", "flag_dir", "parent_dir"])
for i in lst:
    i = i.split(", ")
    dir_1 = Direct(i[0], i[1], i[2], i[3])
    logger.info(msg=f" result: {dir_1}")
    print(dir_1)