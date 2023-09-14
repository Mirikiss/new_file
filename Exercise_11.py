def selection():
    number = [int(i) for i in range(2,int(input('от 2 до какого числа выполнить выборку: ')))]
    for i in number:
        counter = 0
        j = 1
        while i >= j:
            if i % j == 0:
                counter += 1
            j += 1
        if counter < 3:
            yield i

for x in selection():
    print(x, end = ' ')


