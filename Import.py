# import Function as F # можно замещать полное название теста Function -> F
# print(F.f(1)) # аналог (Function.f(1))

# def new_string(symbol, count): # 
#     return symbol * count

# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # TypeError missing 1 required ...

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))   # !!!!!
# print(new_string('!'))      # !!!
# print(new_string(4))        # 12

def concatenatio(*params): # * - несколько значений
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))  # Консоль asdw (ф-я складывает строку)
print(concatenatio('a', '1', 'd', '2'))  # Консоль a1d2
# print(conatenatio(1, 2, 3, 4)) # Консоль TypeError: ... (ошибка - работаеv с типом str, чтобы работало с числами прописать int = 0)
# можно просто прописать res = 0 без типа