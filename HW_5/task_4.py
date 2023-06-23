# Создайте функцию генератор чисел Фибоначчи


def fibonacci(n):
    a = 0
    b = 1
    fib_list = []
    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


fibonacci_numbers = fibonacci(10)
print(fibonacci_numbers)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        

fib = fibonacci()
for i in range(10):
    print(next(fib))
