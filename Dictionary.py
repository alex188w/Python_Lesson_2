dictionary = {} # пустой
            # \ чтобы не писать все в одну строку
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])  # ←
# типы ключей могут отличаться

for k in dictionary.keys(): # вывод на экран ключей
    print(k)

for v in dictionary: # вывод на экран ключей
    print(v)

for k in dictionary.values(): # вывод на экран значений
    print(k)

for v in dictionary: # вывод на экран значений
    print(dictionary[v])

print(dictionary['up'])   # ↑
# типы ключей могут отличаться

dictionary['left'] = '⇐'
print(dictionary['left'])  # ⇐
#print(dictionary['type'])  # KeyError: 'type'
del dictionary['left'] # удаление элемента

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →