#dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}


#1

farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = farm_1.intersection(farm_2)

print (farm_3)

#2

farm_1 = {"dog", "cat", "mouse", "sheep"}

farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

far = farm_2.difference(farm_1)

print (far)

#3

get = {'get' , 'go', 'more', 'biz' , 'nes' }
get.add(23)
print (get)
get.pop()
print(get.pop())
