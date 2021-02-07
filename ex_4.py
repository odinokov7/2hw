a = input('Введите строку: ')
b = a.split(' ')
n = 0
for el in b:
    el = el[:10]
    n += 1
    print(n, ' ', el)
