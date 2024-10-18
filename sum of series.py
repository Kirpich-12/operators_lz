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
s = round(s, e) #сокращение числа s до e знаков после запятой 

while sam < poi:
    if poi > 1.65:  #защита от бесконечного цикла
        print('Уход в бесконечный цикл, замените значение финальной суммы')
        break
    else:
        sam += dec(1) / dec(n) ** 2 # приведение типов данных(ругается)
        n += 1 
        print(sam)
else:     
     if sam - poi > poi - (sam - dec(1) / dec(n) ** 2): # -1 если вышли за пределы
        n -= 1
     if poi < 1:
         n -= 1


#вывод данных(выводит 0 при беск. цикле)
output_data = open('output.txt', 'w')
output_data.write(str(n))

#закрытие файлов 
input_data.close()
output_data.close()