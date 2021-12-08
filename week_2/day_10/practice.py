# Задание 1

# Циклы, Условия и массивы - ПОВТОРЕНИЕ
# Давайте представим ситуацию что вы работаете в Тур-Агентстве.

###Страны###

countries_of_east = [Singapore, Malaysia, Indonesia, Hawaii]
countries_of_central_asia = [Kyrgyzstan, Kazakhstan, Tajikistan, Uzbekistan]
countries_of_europe = [Italy, France, Germany, Switzerland, Ireland]
countries_of_america = [Mexico, USA, Brazil, Columbia, Canada]
classes = [Business, Middle, Econom]
#Так получилось что не все рейсы доступны всегда.

# Представьте что есть переменные:
user_order_0 = 'Brazil'
user_order_1 = 'Madagaskar'
user_order_2 = 'Kyrgyzstan'
user_order_3 = 'Italy'
user_order_4 = 'Argentina'
user_order_5 = 'Malasia'

# Классы самолета
class_0 = 'Business'
class_1 = 'Middle'
class_2 = 'Econom'
 
# каждая из этих переменных - заказ пользователя 
#который хочет полететь в указанную страну.

# Так как вы серьёзная компания, у вас имеется ряд правил:

# 1. Если у вас не нашлось билета в страну куда хочет клиент,
# вы ему вежливо говорите: "Простите рейсов в эту страну пока нет..."
# 2. Бизнес класс доступен только для следующих стран:
# Germany, Tajikistan, Hawaii, Canada
# 3. Эконом класс доступен только для следующих стран:
# Kazakhstan, Switzerland, Singapore, Columbia
# 4. Если у вас имеется билет в эту страну -
# вы пишите пользователю следующее:
#        "Ваш рейс найден! Ваш класс {здесь имя класса}".
# 5. Если для этого рейса есть особый класс(Бизнес или Эконом)
# вы выводите именно его иначе по умолчанию стоит "Middle"

biznes = 'Germany', 'Gajikistan', 'Hawaii','Canada'
econom = 'Kazakhstan' , 'Switzerland' , 'Singapore', 'Columbia'


if class_0 in  countries_of_east :
	print ('biznes')
if class_0 in  countries_of_europe:
	print ('biznes')
if class_0 in  countries_of_central_asia:
	print ('biznes')
if class_0 in countries_of_america:
	print ('biznes')


else: 
	print ('vash reis ne naiden')
  
