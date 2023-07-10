import random


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


def random_eight_queens():
    """Генерируем случайную расстановку восьми ферзей"""
    return tuple(random.randint(1, 8) for _ in range(8))


successful_arrangements = []
while len(successful_arrangements) < 4:
    arrangement = random_eight_queens()
    if check_eight_queens(arrangement):
        successful_arrangements.append(arrangement)
        print("Успешная расстановка:", arrangement)

print("Всего успешных расстановок:", len(successful_arrangements))
for arrangement in successful_arrangements:
    print(arrangement)
