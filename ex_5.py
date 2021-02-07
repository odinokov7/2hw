my_list = [7, 5, 4, 3, 3, 3, 3, 2, 1]
b = 0
a = int(input('Введите число: '))
c = 0

print(my_list)

for el in my_list:
    c += 1
print('Кол-во эл: ', c)

if a > my_list[0]:
    my_list.insert(0, a)
elif a <= my_list[c - 1]:
    my_list.append(a)
else:
    for el in my_list:
        if a > el:
            b = my_list.index(el)
            break
    print('Номер элемента для вставки: ', b)
    my_list.insert(b, a)

print(my_list)
