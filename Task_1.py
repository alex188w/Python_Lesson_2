# with open('file.txt', 'w') as data:
#     data.write('text 121 1\n')
#     data.write('text 125 2\n')
   

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nline text 1\n')
# data.write('line text 2\n')
# data.close()


path = 'file.txt' # путь к файлу (path, data - переменные)
data = open(path, 'r') # режим чтения
for line in data:  
    print(line) # считать построчно
data.close()