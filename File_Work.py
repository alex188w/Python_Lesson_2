path = 'file_1.txt'
# # связывание переменной с файлом path
f = open(path, 'r')
data = f.read() + ' ' # считываем все что есть и добавляем пробел для работы в цикле
f.close()

numbers = []

while data != '': # проверка: пока строка не пустая (для этого сделаны пробелы)
     space_pos = data.index(' ') # позиция первого пробела (добавить в список номеров)
     numbers.append(int(data[:space_pos])) # взять все что находится от пирвого символа до первого пробела и превратить в число и добавить в список чисел
     data = data[space_pos + 1:] # перейти к следующей строке

out = [] # 
for e in numbers:
    if not e % 2: # проверка четности числа
        out.append((e, e**2)) #

print(out)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split() # функция split( позволяет превратить список в набор строк
# res = select(int, data) # на выходе получается список чисел
# res = where(lambda e: not e % 2, res)
# res = list(select(lambda e: (e, e**2), res))
# print(res)

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split() # функция split( позволяет превратить список в набор строк
# res = map(int, data) # на выходе получается список чисел
# res = where(lambda e: not e % 2, res)
# res = list(map(lambda e: (e, e**2), res))
# print(res)


data = '1 2 3 5 8 15 23 38'.split() # функция split( позволяет превратить список в набор строк
res = map(int, data) # на выходе получается список чисел
res = filter(lambda e: not e % 2, res)
res = list(map(lambda e: (e, e**2), res))
print(res)