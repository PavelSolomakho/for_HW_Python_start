def check_attack(x1, y1, x2, y2):
    """Проверяем, бьют ли два ферзя друг друга"""
    return (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2))


def check_attack(x1, y1, x2, y2):
    """Проверяем, бьют ли два ферзя друг друга"""
    return (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2))


def check_eight_queens(arrangement):
    """Проверяем, не бьют ли восьмь ферзей друг друга"""
    for i in range(8):
        for j in range(i+1, 8):
            if check_attack(i+1, arrangement[i], j+1, arrangement[j]):
                return False
    return True


# Запрос расстановки ферзей у пользователя
print("Введите координаты 8 ферзей (числа от 1 до 8, разделенные пробелами):")
arrangement = tuple(map(int, input().split()))

# Проверка расстановки ферзей и вывод результата
if check_eight_queens(arrangement):
    print("Ферзи не бьют друг друга.")
else:
    print("В расстановке есть пара бьющих друг друга ферзей.")
