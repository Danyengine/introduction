'''
min_1 = 60
hour_1 = 3600
day_1 = 3600*24


def data_time(sec):
    
    # Вывод до минуты:
    if sec < min_1:
        return (sec, 'secands')
    
    # Вывод до часа:
    elif min_1 <= sec < hour_1:
        minuts = sec // 60  # целое от деления
        sec = sec % min_1
        return ('{} мин {} сек'.format(minuts, sec))
    
    # Вывод до дня:
    elif  hour_1 <= sec < day_1:
        hours = sec // 3600
        sec %= hour_1
        minuts = sec // min_1
        sec = sec % min_1
        return ('{} ч {} мин {} сек'.format(hours, minuts, sec))
    
    # Вывод до года:
    elif sec >= day_1:
        days = sec // day_1
        sec %= day_1
        hours = sec // hour_1
        sec %= hour_1
        minuts = sec // min_1
        sec %= min_1
        return ('{} дн {} ч {} мин {} сек'.format(days, hours, minuts, sec))

duration = int(input('Введите текущее время в секундах: '))
print(data_time(duration))
'''



# list of uneven numbers cubed
cube_lst = []

for num in range(1,1001):
    if num % 2 != 0:
        cube_lst.append(num**3)

#print(cube_lst) 





cube_even_7 = [] # list of numbers that (% 7 == 0)


for i in range(len(cube_lst)):

    num = cube_lst[i]
    sum_numbers = 0     # сумма цифр i-го числа
    while num != 0:
        sum_numbers += num%10
        num //=10
    if sum_numbers % 7 == 0:
        cube_even_7.append(cube_lst[i])

print(cube_even_7)

# Сумма чисел, нацело делящиеся на 7
sum_even_num_7 = 0
for num in cube_even_7:
    sum_even_num_7 += num
print(sum_even_num_7)



for num in cube_lst:
    
    sum_numbers = 0
    while (num != 0):
        sum_numbers += num%10
        num //= 10
        
    if sum_numbers % 7 == 0: 
        numbers_sum.append(cube_lst[i]) # список чисел, сумма цифр которых делится нацело на 7
         
    

sum_num_7 = 0

# сумма чисел, которые делятся нацело на 7
for i in range(len(numbers_sum)):
    sum_num_7 += numbers_sum[i]


print(2**2)

 