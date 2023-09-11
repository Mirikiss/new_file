
def trans_matrixs():

    n = int(input('количество переменных в матрице: '))
    matrix = []

    for i in range(n):
        tmp = [int(i) for i in input('введите числа через пробел: ').split(' ')]
        matrix.append(tmp)

    for i in range(len(matrix[0])):
        for j in range(n):
            print(matrix[j][i], end = ' ')
        print()


if __name__ == '__main__':
    trans_matrixs()