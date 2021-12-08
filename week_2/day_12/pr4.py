list_t_words = []
with open ('python.txt', 'r') as ff:
	for i in ff.read().split():
		if 'T' in i  or 't' in i:
			list_t_words.append(i)
		else:
			print('error')
print(list_t_words)

