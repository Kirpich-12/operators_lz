'''
Посчитать количество итераций, необходимых для того, чтобы сумма членов ряда приблизилась к заданному числу
'''

from decimal import Decimal as dec

input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()

L = dec(data[0])     # изначальная сумма
E = int(data[1])     # точность
S = dec(data[2])     # искомая сумма
count = 1            # количество     
summ = 0             #переменные необходимые для решения

poi = S - L #число которое необходимо добавить к L, следовательно искомая сумма
S = round(S, E)

# поиск количества происходящих итераций
while summ < poi:
    if poi > 1.65:  #защита от бесконечного цикла
        print('Уход в бесконечный цикл, поменяйте значение искомой суммы')
    summ += (1/ count**2)
    count += 1
    if S - L < 1:
        count = 1
    
else:
    if summ - float(S) < float(S) - (summ - 1 / (count - 1)**2):
        count = count - 1
    count -= 1

#вывод данных (будет выводить 0 при бесконечном цикле цикле)
output_data = open('output_1.txt', 'w')
output_data.write(str(count))

#закрытие файлов 
input_data.close()
output_data.close()