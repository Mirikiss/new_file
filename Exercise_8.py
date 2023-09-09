things  = {
        "вилка": 1,
        "ложка": 1,
        "вода": 3,
        "ботинки": 3,
        "куртка": 5,
        "камера": 4,
        "чайник": 4,
        "палатка": 12,
        "еда": 5,
        "джинсы": 4,
        "посуда": 2,
        }

sorted_things = sorted(things.items(), key=lambda para: para[1], reverse=True)

max_bag = int(input('введите допустимый вес рюкзака: '))
s = {}

def bagaj(x, y):
        for a, b in sorted_things:
                if x - b >= 0:                      
                        if a in y:
                                y[a] += b
                                x = x - b
                        else:
                                s.update({a: b})
                                x = x - b
        return x, y

while max_bag > 0:
        max_bag, s = bagaj(max_bag, s)

print(f'оставшийся вес багажа: {max_bag} кг.\nВы можете взять: ')
        
for i, j in enumerate(s.items(), 1):
                print(f'{i:2}. {j[0]:<11} - {j[1]}')



