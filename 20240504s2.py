a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите шаг: "))
result1 = 0
result2 = 0

for i in range(a, b, c):
    result1 += i
    result2 -= i

if a % 2 == 0:
    print(f"Результат: {result1}")
elif a % 2 != 0:
    print(f"Результат: {result2}")
