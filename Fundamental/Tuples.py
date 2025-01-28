t = (10, 20, 30, 40)

print(t)
print(type(t))
print(len(t))
print(t[0])



t = (10, "Hello", 2.85)
print(t)

print(t[0])
print(type(t[0]))
print(t[1])
print(type(t[1]))
print(t[2])
print(type(t[2]))
print(t[-2])
print(type(t))
print(len(t))


t = (10, "Hello", 2.85)
t1 = t + (56.5, 'Python', 99)
print(t1)


# t[1]= 20 # TypeError: 'tuple' object does not support item assignment
del t1  # Delete the tuple
#del t[0] # TypeError: 'tuple' object doesn't support item deletion 

