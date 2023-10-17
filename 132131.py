def Calculate():
    print(f'{(x:="ТАБЛИЦА УМНОЖЕНИЯ"):^33}')
    for i in [2, 6]:
        for j in range(2, 11):
            a, b, c = i + 1, i + 2, i + 3
            return (f'{i}*{j}={i*j}\t{a}*{j}={a*j}\t{b}*{j}={i*b}\t{c}*{j}={c*j}')
        #print()

#Calculate()

