# Задание №1:

# Если взять ВСЕ числа от 0 до 10, которые деляться на 3 или 5 БЕЗ ОСТАТКА, то получим 3, 5, 6 и 9. 
# Сумма этих чисел равна 23 (3+5+6+9) = 23.

# Найдите сумму всех чисел меньше 1000, кратных 3 или 5

a = [x for  x in range(1,1000) if x %3==0 or  x%5==0]
print (sum(a))
 
#reshesni nomer 2


'''total = 0
b =0

for i in range (1000):
	if i %3==0 and i % 5 == 0:
	total +=1
	b += 1
print (total * b)'''


#Задание 2
# a = 333
# b = 555
# Поменяйте значения переменных местами(НЕ ВРУЧНУЮ!), чтобы в ПЕРЕМЕННОЙ "a" было значение 555, а в ПЕРМЕННОЙ "b" было значение 333.

a = 333
b = 555
a,b = b,a
print (a,b)


#Задание №3:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.


num = "4729461084"
x = [int(a) for a in str(num)]
print(sum(x))  


# Задание №4:
# Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30"
# и возвращает dictionary разделённую по значениям даты:

# date = {
# "year": "2020",
# "month": "10",
# .....
# }

'''a = input (vvedite day i vremya)

dict = {''year'': }'''



#5

word = 'qwer'
i = 0
while i < 5:
	word = word + word
	i += 1
print (i)
