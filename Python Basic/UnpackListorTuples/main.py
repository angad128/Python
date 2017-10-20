#date, item, price = ['Dec 23 2017', 'Pendrive', 800]
#print(price)

def drop_first_last(grades):
    first , *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

listA= [70,30,40,40,70,60]
listB= [4,3,5,2]

drop_first_last(listA)
drop_first_last(listB)




