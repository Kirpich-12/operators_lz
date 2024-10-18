data_s =  open('input.txt', 'r')
n = int(data_s.read())

prs = []
ans = 'N'

for i in range(1,n + 1):
    if n % i == 0:
        prs.append(i) #кол-во делителей числа n+

if len(prs) == 2: # у простого числа 2 делителя(1 и само число )
    ans = 'Y'

output_data = open('output.txt', 'w')
output_data.write(ans)
#запись

data_s.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать