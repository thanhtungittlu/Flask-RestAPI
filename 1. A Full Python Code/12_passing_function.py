def methodception(another):
    return another()
def add_sum_number():
    return 10 + 20

print(methodception(add_sum_number))

print(methodception(lambda: 10+20))

my_list = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, my_list)))

def even_number(x): # Trả về true nếu là số chẵn
    return (x % 2 == 0)   

print(list(filter(even_number, my_list)))

print([x for x in my_list if x %2 == 0])


## 2 cái này tương đương nhau:
(lambda x: x * 3)(5)

def funciton(x):
    return x*3
funciton(5)

