import csv
from random import randint


def deco_csv(function: Callable):
    create




def deco_csv(function: Callable):
    create_coefficients_csvfile()

    def wrapper():
        with open('coefficiens_of_equation.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coef in data:
                if coef and coef[0] != 0:
                    function(*coef)

    return wrapper