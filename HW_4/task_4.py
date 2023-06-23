transactions = []  # создаем пустой список для хранения транзакций


def deposit(amount, balance):
    """
    Функция для пополнения баланса на указанную сумму.

    :param amount: сумма пополнения.
    :param balance: текущий баланс.
    :return: новый баланс.
    """
    new_balance = balance + amount
    transactions.append(('deposit', amount))  # добавляем транзакцию в список
    return new_balance


def withdraw(amount, balance):
    """
    Функция для снятия указанной суммы со счета.

    :param amount: сумма снятия.
    :param balance: текущий баланс.
    :return: новый баланс.
    """
    if amount > balance:
        raise ValueError("Недостаточно средств на счете.")
    new_balance = balance - amount
    # добавляем транзакцию в список
    transactions.append(('withdrawal', amount))
    return new_balance


def main_menu(balance):
    """
    Функция для отображения главного меню и обработки выбора пользователя.

    :param balance: текущий баланс.
    :return: новый баланс после выполнения выбранной операции.
    """
    while True:
        print("Текущий баланс:", balance)
        print("Выберите операцию:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Выйти из меню")

        choice = input("Введите номер операции: ")
        if choice == "1":
            amount = int(input("Введите сумму пополнения: "))
            balance = deposit(amount, balance)
        elif choice == "2":
            amount = int(input("Введите сумму снятия: "))
            try:
                balance = withdraw(amount, balance)
            except ValueError as e:
                print(e)
        elif choice == "3":
            break
        else:
            print("Некорректный выбор операции.")

    return balance


# Пример использования функций
balance = 1000  # начальный баланс

# Предоставляем пользователю выбор операции
balance = main_menu(balance)

# Выводим список всех транзакций
print("Список всех транзакций:")
for transaction in transactions:
    print(transaction)
