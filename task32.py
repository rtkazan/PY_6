from random import randint

max = int(input("Введите максимальное число массива: "))
min = int(input("Введите минимальное число массива: "))
volume = int(input('Введите размер массива: '))
array = [randint(-10, 20) for i in range(int(volume))]
print(array)

for i in range(len(array)): 
    if min <= array[i] <= max: 
        print(i, end=' ')