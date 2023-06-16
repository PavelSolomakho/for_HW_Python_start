def get_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates


# Запрос списка у пользователя
user_input = input("Введите список чисел через пробел: ")
my_list = [int(item) for item in user_input.split()]

# Вызов функции для поиска дубликатов и вывод результата
duplicates = get_duplicates(my_list)
print(f"Список дубликатов: {duplicates}")
