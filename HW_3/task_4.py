# создаем словарь со списком вещей для похода и их массой
items = {
    'спальный мешок': 1,
    'палатка': 2,
    'каримат': 0.5,
    'горелка': 0.3,
    'еда': 1.5,
    'вода': 2,
    'кувшин': 0.6,
    'топор': 1.2,
    'нож': 0.2,
    'фонарик': 0.4
}

# задаем максимальную грузоподъемность рюкзака
max_weight = 10


def find_combinations(items, max_weight):
    # создаем список возможных комбинаций вещей
    combinations = [[]]
    for item_name, item_weight in items.items():
        new_combinations = []
        for c in combinations:
            if sum([items[i] for i in c]) + item_weight <= max_weight:
                new_combinations.append(c + [item_name])
        combinations += new_combinations
    return combinations[1:]


# выводим все возможные варианты комплектации рюкзака
for combination in find_combinations(items, max_weight):
    print(combination)
