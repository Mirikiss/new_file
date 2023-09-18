def check_queen(nums: list):
    numbers = nums
    #numbers = [1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]
    n = 8

    x = [0]*8
    y = [0]*8

    for i in range(n):
        x[i], y[i] = numbers[i]

    Flag = True

    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    Flag = False
    if Flag:
        return(True) 
    else:
        return(False)

import random
def selection_queen(selection):
     numbers = []
     n = 8
     counter = 0
     while counter <= selection:
         i = 0
         while i < n:
             x = random.randint(1,8)
             y = random.randint(1,8)
             if [x, y]  not in numbers:
                 numbers.append([x,y])
                 i+=1
         if check_queen(numbers):
             print(numbers)
             counter += 1
         numbers.clear()


