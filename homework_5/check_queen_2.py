from check_queen_1 import check_queen, selection_queen


if __name__ == '__main__':
    print(check_queen([list(map(int, input('введите числа через пробел: ').split(' '))) for _ in range(8)]))

    #print(selection_queen(int(input('введите количество: '))))
