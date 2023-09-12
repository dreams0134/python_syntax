# Оператор for (55 строка так-то)

# "чтение" значения объекта с последовательностью по порядку
# считанное значение присваивается в собственную переменную
# выполняет код своего тела

lst_0 = [10, 20, 30, 4, 3, 100]

# for value in lst_0:
#     value *= 10
#     print(value)

# for char in "python":
#     print(char)

dict_0 = dict(a=100, b=200, c=300)

# print(dict_0)

# for item in dict_0.items():
#     print(item)

# for k, v in dict_0.items():
#     print(f"Ключ: {k}, Значение: {v}")

# for k in dict_0.keys():
#     print(f"Ключ: {k}") 

# класс range() (технически ведет себя как функция и считать функцией не возбраняется)

r = range(-10, 20, 2) #range работает только с целочисленными значениями

# print(r)
# print(tuple(r))

# for n in range(-5, 5):
#     print(n)

# for n in range(-5, 5):
#     print("hello")

for n in range(5):
    print("hello")

# самостоятельно - генератор списка, кортежа
# генератор словаря