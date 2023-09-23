from random import randint as rnd

def find_number(min_nmb: int, max_nmb: int, counter: int):
    nmb = rnd(min_nmb, max_nmb)
    print(nmb)
    i = 2
    s = int(input('введите число: '))
    while i <= counter:
        if s == nmb:
            return 'нашёл'
        elif s > nmb:
            print('больше')
        elif s < nmb:
            print('меньше')
        s = int(input('введите число: '))
        i+=1
    else:
        return 'поппытки закончились'
        
print(find_number(1, 10, 5))


