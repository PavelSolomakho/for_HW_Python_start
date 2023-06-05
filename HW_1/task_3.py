from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print(f"Я загадал число от {LOWER_LIMIT} до {UPPER_LIMIT}.")
for attempt in range(MAX_ATTEMPTS):
    guess = int(input(f"Попытка №{attempt+1}: "))
    
    if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
        print("Некорректный ввод! Попробуйте еще раз.")
        continue
        
    if guess == num:
        print(f"Поздравляю! Вы угадали число {num} за {attempt+1} попыток!")
        break
    elif guess < num:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
else:
    print(f"Увы, вы не смогли угадать число {num} за {MAX_ATTEMPTS} попыток.")
    