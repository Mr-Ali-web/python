import sys 

x = [1,2,3,4,5,6,7,8,9,10]
a = x 
print("a:", a)



a = 5
b = 5

a = b 
print("a == b:", a == b)


a = [1, 2, 3]
b = a[:]
b.append(4)
print(a,b)

a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a,b)

