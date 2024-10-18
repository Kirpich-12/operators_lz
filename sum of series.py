from decimal import Decimal as dec

input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()

l = dec(data[0])
e = int(data[1])
s = dec(data[2])
n = 1
sam = 0             #переменные необходимые для решения

poi = s - l #число которое необходимо добавить к l, следовательно искомая сумма
s = round(s, e)#

while sam < poi:
    if poi > 1.65:  #защита от бесконечного цикла
        print('Уход в бесконечный цикл, замените значение финальной суммы')
        break
    sam += (1/ n ** 2)
    n += 1
    if s - l < 1:
        n = 1
    
else:
    if n != 1:
        if sam - float(s) < float(s) - (sam - (1/ (n -1) ** 2)):
            n = n - 1
    else:
        n == 0
    n -= 1

#вывод данных(выводит 0 при беск. цикле)
output_data = open('output.txt', 'w')
output_data.write(str(n))

#закрытие файлов 
input_data.close()
output_data.close()