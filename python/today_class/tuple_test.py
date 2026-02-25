t1 = ()
print(type(t1))

t2 = (10, )
print(type(t2))
print(t2)

t3 = (1, 2, 3)
print(t3)

t4 = 1, 2, 3 # packing
print(t4)

x ,y , z = t4 # unpacking
print(x, y, z)

t5 = (1, 10.5 , "Python")
print(t5)
print(t5[2])
print(t5[2][0:2])
t5[2] = "Java" # tuple은 불변함수

a = (1, 2, 3, [4, 5])
a[3][0] = 10
print(a)