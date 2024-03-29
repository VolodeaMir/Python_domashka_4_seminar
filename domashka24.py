# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


n = int(input())  # считываем количество кустов на грядке
a = list(map(int, input().split()))  # считываем урожайность кустов
max_harvest = 0  # переменная для хранения максимальной урожайности
for i in range(n):
    # вычисляем урожайность при сборе с i-го куста и двух его соседей
    harvest = a[i] + a[(i-1) % n] + a[(i+1) % n]
    if harvest > max_harvest:
        max_harvest = harvest
print(max_harvest)  # выводим максимальную урожайность
