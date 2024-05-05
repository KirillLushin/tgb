# Считываем данные
a = int(input("Введите первое число: "))
operator = input("Введите математический оператор (+, -, *, /): ")
b = int(input("Введите второе число: "))

# Производим вычисления
if operator == "+":
 result = a + b
elif operator == "-":
 result = a - b
elif operator == "*":
 result = a * b
elif operator == "/":
 if b != 0:
     result = a / b
 else:
     print("Ошибка: деление на ноль")
else:
 print("Неизвестный оператор")


# Выводим результат
print(f"Результат: {result}")