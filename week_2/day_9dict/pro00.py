menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu ['besh_barmak'] = 130


print (menu)

a = {'besh_barmak': 135}

menu.update(a)

print (menu)

menu.pop('borsh')

print (menu)
