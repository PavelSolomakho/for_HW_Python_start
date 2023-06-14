def int_to_hex_string(number):
    hex_string = hex(number)[2:]
    return hex_string.upper()


# Запрос ввода числа у пользователя
decimal_num = int(input("Введите целое число: "))

# Преобразование числа в шестнадцатеричную строку и вывод результата
hex_str = int_to_hex_string(decimal_num)
print(f"Шестнадцатеричное представление числа {decimal_num} равно: {hex_str}")
