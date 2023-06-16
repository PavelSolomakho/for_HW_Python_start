def keyword_args_to_dict(*args, **kwargs):
    result = {}
    for key in kwargs:
        if isinstance(key, (int, float, str, tuple, frozenset)):
            # если ключ хешируемый, используем его напрямую
            result[key] = type(kwargs[key]).__name__
        else:
            # если ключ не хешируемый, используем его строковое представление
            result[str(key)] = type(kwargs[key]).__name__
    for arg in args:
        if isinstance(arg, (int, float, str, tuple, frozenset)):
            # если аргумент хешируемый, используем его напрямую
            result[arg] = type(arg).__name__
        else:
            # если аргумент не хешируемый, используем его строковое представление
            result[str(arg)] = type(arg).__name__
    return result

# вызываем функцию и выводим результаты
#print(keyword_args_to_dict(1, 'hello', [1, 2, 3]))
print(keyword_args_to_dict(x=1, y='hello', z=(1, 2, 3)))
