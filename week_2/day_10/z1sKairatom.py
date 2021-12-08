Tent1703

# Задание 1
# Циклы, Условия и массивы - ПОВТОРЕНИЕ
# Давайте представим ситуацию что вы работаете в Тур-Агентстве.
 
###Страны###
 
countries_of_east = ['Singapore', 'Malaysia', 'Indonesia', 'Hawaii']
countries_of_central_asia = ['Kyrgyzstan', 'Kazakhstan', 'Tajikistan', 'Uzbekistan']
countries_of_europe = ['Italy', 'France', 'Germany', 'Switzerland', 'Ireland']
countries_of_america = ['Mexico', 'USA', 'Brazil', 'Columbia', 'Canada']
classes = ['Business', 'Middle', 'Econom']
# Так получилось что не все рейсы доступны всегда.
countries_list=[countries_of_east,countries_of_central_asia,countries_of_europe,countries_of_america]
# # Представьте что есть переменные:
user_order_0 = 'Brazil'
user_order_1 = 'Madagaskar'
user_order_2 = 'Kyrgyzstan'
user_order_3 = 'Italy'
user_order_4 = 'Argentina'
user_order_5 = 'Malasia'
order_list=[user_order_0,user_order_1,user_order_2,user_order_3,user_order_4,user_order_5]
# # Классы самолета
class_0 = 'Business'
class_1 = 'Middle'
class_2 = 'Econom'

business_class=['Germany', 'Tajikistan', 'Hawaii', 'Canada']
econom_class=['Kazakhstan', 'Switzerland', 'Singapore', 'Columbia']
 
# каждая из этих переменных - заказ пользователя который хочет полететь в указанную страну.

# Так как вы серьёзная компания, у вас имеется ряд правил:

# 1. Если у вас не нашлось билета в страну куда хочет клиент, вы ему вежливо говорите: "Простите рейсов в эту страну пока нет..."
# 2. Бизнес класс доступен только для следующих стран: Germany, Tajikistan, Hawaii, Canada
# 3. Эконом класс доступен только для следующих стран: Kazakhstan, Switzerland, Singapore, Columbia
# 4. Если у вас имеется билет в эту страну - вы пишите пользователю следующее:
# "Ваш рейс найден! Ваш класс {здесь имя класса}".
# 5. Если для этого рейса есть особый класс(Бизнес или Эконом) вы выводите именно его иначе по умолчанию стоит "Middle"
############################################################################

# Решение:

while True:
    if order_list:
        for region in countries_list:
            for u_o in order_list:
                for b_c in business_class:
                    if u_o in b_c and u_o in region:
                        print(f"Ваш рейс найден! Ваш класс {class_0}")
                        break
                    else:
                        print(f"Ваш рейс не найден! Ваш класс {class_1}")
                        break
                for e_c in econom_class:
                    if u_o in e_c and u_o in region:
                        print(f"Ваш рейс найден! Ваш класс {class_2}")
                        break
                    else:
                        print(f"Ваш рейс не найден! Ваш класс {class_1}")
                        break
 else:
	 print("Простите рейсов в эту страну пока нет...")
       	 break
    break

