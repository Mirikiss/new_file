import csv
import datetime
import json
from math import sqrt
import os.path
from random import randint as rnd
from typing import Callable

def generate_csv_file(name_file, counter):
    with open(name_file, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        for _ in range(counter):
            row = [rnd(1,1000) for _ in range(3)]
            writer.writerow(row)


def find_discriminant(*args):
    a, b, c = args
    discriminant = b ** 2 - 4 * a * c
    print(discriminant)
    if discriminant > 0:
        x1 = (-b + sqrt(discriminant) / 2*a)
        x2 = (-b - sqrt(discriminant) / 2*a)
        return round(x1,2), round(x2,2)
    elif discriminant == 0:
        x = -b / 2*a
        return round(x, 2)
    else:
        return None

print(find_discriminant(1, 5, 2))



