import random
lists = [random.randint(1,10) for _ in range(20)]
print('Сам список: ', lists)

new_lists = set([i for i in lists if lists.count(i) > 1])
error_lists = set([i for i in lists if lists.count(i) == 1])

print('Осталось: ', *new_lists, 'Было удалено: ', *error_lists)