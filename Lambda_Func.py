# def sum(x):
#     return x+10

# def mult(x):
#     return x**2

# print(sum(mult(2)))

# sum = lambda x: x+10
# mult = lambda x: x**2

# print(sum(mult(2)))

# def f(x):
#     x**2

# g = f
# print(f(2))
# print(g(2))

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc2, 10)

def sum(x, y):
    return x+y

# def mult(x, y):
#     return x*y

#f = mult

mult = lambda x, y: x*y # короткая запись

# def calc(op, a, b):
#     print(op(a, b))
#     return op(a, b)    

# calc(mult, 4, 5)
# #calc(f, 4, 5)
# calc(lambda x, y: x*y, 4, 5)

# List Comprehetion

# list = []

# for i in range(1, 21):
#     if i%2 == 0:
#         list.append(i);

# Укороченная запись того же
# 
# li = [x for x in range(1, 10)]

# li = list(map(lambda x:x+10, li)) # map  - хорощая замена select
# print(li)

#data = list(map(int, input().split())) # есть набор данных вводим через пробел (функция split позволяет превратить список в набор строк)
                                                #(если хотим разделить запятой, то ',' - по умолчанию пробелы)
                                                # превращаем из спика строк в список чисел
#print(data)

# data = map(int, input().split())

# for e in data:
#     print(e)

# data = list(map(int, '1 3 45 67 89'.split()))

# for e in data:
#     print(e)

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
zarplata = [555, 777, 999]
data = list(zip(users, ids, zarplata))
print(data) # проходит по минимальному списку

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)
