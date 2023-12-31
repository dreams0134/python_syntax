# Операции/оператор сравнения (тождественно)

x = -3
y = 3

# операции равенства (равно)
# мы спрашиваем "значение x равно значению y?"
res = x == y

# операции неравенства (не равно)
# мы спрашиваем "значение x НЕ равно значению y?"
res = x != y

# операция "меньше"
# мы спрашиваем "значение x меньше значения y?"
res = x < y

# операция "меньше"
# мы спрашиваем "значение x меньше значения y?"
res = x > y

# операция "меньше либо равно"
# мы спрашиваем "значение x меньше либо равно значению y"
x = 3
res = x <= y

# операция "меньше либо равно"
# мы спрашиваем "значение x меньше либо равно значению y"
res = x >= y


#логические операции

v_1 = True
v_2 = False

# оператор "НЕ" (NOT, инверция, отрицание)
res = not v_1

# оператор "и" (AND, конъюкция, логическое умножение)
# возвращает Trye только тогда, когда оба значения True
res = v_1 and v_2

# операция "или" (OR, дизъюкция, логическое сложение)
# возвращает False 
res = v_1 or v_2



a = 10
b = 0
c = -5

res = (a > b) or not (b == c)

# ****
# отступы в языке python очень важны
# по отступам интерпретатор ориентируется во вложенности кода
# Tab - перемещение вправо на один отступ
# Shift + Tab - перемещекние влево на один отступ
# ****


#условие операции

a = -10

# оператор if (если)
# if a == 0:
#     print("hello!") #здесь без отступа (идет по умолчанию) будет ошибка, вернуть отступ можно клавишей табуляции (Tab)

# оператор else (иначе)
# if a > -1: #двоеточние не забывать
#     res = "больше минус одного"
# else:
#     res = "меньше либо равно минус одному"

# оператор elif (else if, в Java и С так и идет)
a = 0

if a > 0:
    res = "больше нуля"
elif a < 0:
    res = "меньше нуля"
else:
    res = "равно нулю"

# print(res)


char = 'd'

if char == 'a':
    res = "буква a"
elif char == 'b':
    res = "буква b"
elif char == 'с':
    res = "буква c"
else:
    res = "этот символ я не знаю :("

print(res)