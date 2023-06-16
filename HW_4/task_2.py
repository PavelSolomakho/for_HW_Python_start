def transpose_matrix():
    # Получаем от пользователя количество строк и столбцов матрицы
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    # Инициализируем пустую матрицу
    matrix = []

    # Заполняем матрицу значениями, введенными пользователем
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input("Введите элемент [{}, {}]: ".format(i+1, j+1)))
            row.append(value)
        matrix.append(row)

    # Транспонируем матрицу
    result = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    # Возвращаем результат
    return result


# Вызываем функцию для транспонирования матрицы
transposed_matrix = transpose_matrix()

# Выводим результат на экран
print("Транспонированная матрица:")
for row in transposed_matrix:
    print(row)
