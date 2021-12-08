Задача 4:
# # Напишите проверку на то, является ли строка палиндромом. 
# # Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево.


words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar',
 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which',
 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]

for i in words:
	if i.lower() == i[::-1].lower():
		print(i, "-ero slovo palindrom")
	else:
		print(i, '- eto obychnoe slovo')
