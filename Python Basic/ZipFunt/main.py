first = ['angad', 'tom', 'john']
last = ['Budhathoki','Hanks','Snow']

print(first + last)

names = zip(first, last)
for a,b in names:
    print(a)
    print(a, b)