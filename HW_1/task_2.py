num = int(input("Введите целое число (от 0 до 100000): "))

# Проверяем ограничения на ввод
if num < 0 or num > 100000:
    print("Некорректный ввод")
else:
    # Проверяем является ли число простым
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, " - составное число")
                break
        else:
            print(num, " - простое число")
    else:
        print(num, " - не является ни простым, ни составным числом")
        