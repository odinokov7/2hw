last_elem = 0
n = 0
c = 0
c1 = 0
list_ed = []
list_tmp = []
list_or = list(input('Введдите список: '))

for el in list_or:
    c += 1

print(list_or)
c2 = c

if c % 2 != 0:
    last_elem = list_or[c - 1]
    list_or.pop(c - 1)
    c2 = c - 1

for el in list_or:
    if n < c2:
        list_tmp.append(list_or[n + 1])
        list_tmp.append(list_or[n])
        list_ed.extend(list_tmp)
        n += 2
        list_tmp = []
    else:
        break

if c % 2 != 0:
    list_ed.append(last_elem)

print(list_ed)

