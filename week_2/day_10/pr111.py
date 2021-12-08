'''countries_of_east = ['Singapore', 'Malaysia',' Indonesia',' Hawaii'] 
countries_of_central_asia = ['Kyrgyzstan', 'Kazakhstan', 'Tajikistan', 'Uzbekistan']
countries_of_europe = ['Italy', 'France', 'Germany', 'Switzerland', 'Ireland']
countries_of_america = ['Mexico', 'USA', 'Brazil', 'Columbia', 'Canada']
classes = ['Business', 'Middle', 'Econom']
'''

user_order_0 = 'Brazil'
user_order_1 = 'Madagaskar'
user_order_2 = 'Kyrgyzstan'
user_order_3 = 'Italy'
user_order_4 = 'Argentina'
user_order_5 = 'Malasia'


# Классы самолета
class_0 = {'Business': ["Brazil","Germany", "Tajikistan", "Hawaii", "Canada"]}
class_1 = {'Middle'}
class_2 = {'Econom': ["Kazakhstan", "Switzerland", "Singapore", "Columbia"]}

for user_order_0 in class_0["Business"] or class_2["Econom"] or class_1["Middle"]:
	if user_order_0 == class_0["Business"] or user_order_0 == class_2["Econom"]:
		print ("vash reis naiden")
	else:
		print ("Vash bilet ne naiden")

for user_order_1  in class_0['Business'] or class_2['Econom'] or class_1['Middle']:
	if user_order_0 == class_0['Business'] or user_order_0 == class_2['Econom']:
		print ('vash reis naider')
	else: 
		print('vash reis ne naiden!')
for user_order_2 in class_0['Business'] or class_2['Econom'] or class_1['Middle']:
	if user_order_2 == class_0['Business'] or user_order_0 == class_2['Econom']:
		print ('vash reis naiden! vash klass "Econom"')
	else: 
		print ('vash reis ne naiden!')

for user_order_3 in class_0['Business'] or class_2['Econom'] or class_1['Middle']:
	if user_order_3 != class_0['Business'] or user_order_3 != class_2['Econom']:
		print ('vash reis naiden')
	else:
		print ('vash reis ne naiden')
for user_order_4 in class_0['Business'] or class_2['Econom'] or class_1['Middle']:
	if user_order_4 != class_0['Business'] or user_order_4 != class_2['Econom']:
		print ('vash reis naiden!')
	else:
		print ('vash reis ne naiden')
for user_order_5 in class_0 ['Business'] or class_2['Econom'] or class_2['Middle']:
	if user_order_5 != class_0 ['Business'] or user_order_5 != class_2['Econom']:
		print ('vash reis naiden!')
	else: 
		print ('Vash reis ne naiden')
