# *** Коллекции ***

# Кортеж (tuple)

# упорядоченная (проиндексированная) неизменяемая (иммутабельная) коллекция

# нельзя добавлять
# нельзя заменять
# нельзя удалять

# создание предварительно заполненного кортежа
t_0 = (10, 20, 30, 0, 5, 3)
t_1 = tuple([10, 500, 3.14, "python"])
t_2 = tuple("hello, tuple!")

# чтение значений
v_0 = t_2[0]
v_0 = t_2[-1]

# срез кортежа
s_0 = t_2[:10]
s_0 = t_2[3:9]
s_0 = t_2[::2]
s_0 = t_2[::-1]
s_0 = t_2[-4:-10:-1]

# методы кортежа
t_3 = (1,2,1,1,2,3)

res = t_3.count(1)
res = t_3.index(1, 3, 5)

# print(res)


# Словарь (dict, dictionary)

# неупорядоченная изменяемая коллекция 

# элемент словаря пара "ключ-значение"

# создание пустого слоя
d_1 = {}
d_1 = dict()

# создание предварительно заполненного словаря
d_2 = {5:1000, 0: 3.14, 'A':200, "abc":"python", "кортеж":{1,2,3}}
d_3 = dict([(10, 20), ('k', 'v'), (2, d_2)])
d_3 = dict(a=100, b=200)

# чтение значения
v_1 = d_2["кортеж"]
v_1 = d_2[0]

# v_1 = d_2['D']
# print(v_1)

# замена значения
d_2['A'] = 777

# добавление значения
d_2['B'] = 100
d_2['C'] = 200

# удаление пары
del d_2['B']

# методы
print(d_2)

v_1 = d_2.get('D', 0)

i_0 = list(d_2.items())

v_0 = tuple(d_2.values())

k_0 = tuple(d_2.keys())

print(k_0)

# остальные методы
# множество (set)