a = [1,2,3,4,5]
a[3]=a[1]
print(a)

nums = [1,2,3]
print (nums + [4,5,6])
print (nums * 3)

words = ['spam','egg','spam','sausage']

print ('spam' in words)
print ('tomato' in words)


num = [10,9,8,7,6,5]
num[0] = num[1]-5
print (num)


ew = [1,2,3]
print (not 4 in ew)
print (4 not in ew)
print (not 3 in ew)
print (3 not in ew)


we = [9,8,7,6,5]
we.append(4)
print (we)

we.insert(2,11)
print(we)
print(len(we))


i = 3
while i >=0:
	print (i)
	i=i-1
