import Back
from Back import dis_calc

a = float(input("Введите первый аргумент: "))
b = float(input("Введите второй аргумент: "))
c = float(input("Введите третий аргумент: "))

d = dis_calc(a, b, c)
print("Ответ: ", d)