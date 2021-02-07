list_mes = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
dict_mes = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
a = int(input('Введите число от 1 до 12: '))

if a not in range(1, 13, 1):
    print('Неверное число')
else:
    for key, value in dict_mes.items():
        if a in value:
            print(key)

    if a in list_mes[0]:
        print('Зима')
    elif a in list_mes[1]:
        print('Весна')
    elif a in list_mes[2]:
        print('Лето')
    else:
        print('Осень')
