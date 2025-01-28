d = {'USA':100,'UK':200,'India':300}

print(d)
print(len(d))


d = {'USA':'America','UK':[200,'London'],'India':(300, 400)}
print(d)
print(len(d))


d = {'USA':100,'UK':200,'India':300}
# print(d[0]) # Error

print(d['USA'])
print(d['UK'])
# print(d['uk']) # Error
print(d['India'])

print(d)
d['Aus'] = 500
print(d)

del(d['UK'])
# del[d[0]] # Error
print(d)
print(d.values())
print(d.keys())

for i in d:
    print(i, d[i])

## Range should not be used

print('UK' in d) # Error
print('Aus' in d) 


d1 = {'USA':100,'UK':200,'India':300}
d2 = {'USA':100,'UK':200,'India':300}

print(d1 is d2) # False
print(d1 == d2) # True


d1 = {'USA':100,'UK':200,'India':300}
d2 = {'India':300, 'USA':100,'UK':200}

print(d1 == d2) # True

d2 = d1
print(d1 is d2) # True