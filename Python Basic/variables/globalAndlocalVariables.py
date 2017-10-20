x= 6
def example():
    z= 5
    global x
    print(x)
    print(x+z)
    x+=1
    print(x)
example()

y =2
def example2():
    globx = y
    print(globx)
    return globx
y = example2()
print(y)