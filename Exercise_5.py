print('Загадайте число от 1 до 100 включительо, а комопьютер отгадает')
print('Поехали')
numbers = [25, 12, 6, 3, 2, 1, 1]
number = 50
count = 0
print(number)
answer = input('Верно? (да/нет)')
while answer:
    answer = input('Это число больше загаданного? (больше/меньше/если верно пишем "да"))')
    if answer == 'да' or count == 7:
        #print('Было не легко))) Спасибо за внимание')
        break
    elif answer == 'больше':
        number = number - numbers[count]
        print(number)
    else:
        number = number + numbers[count]
        print(number)
    count += 1
print('Было не легко))) Спасибо за внимание' if answer == 'да' else 'Извините, я не справился')