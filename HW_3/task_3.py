import re
from collections import Counter

text = """
Python - это интерпретируемый, высокоуровневый язык программирования общего назначения. Философия дизайна Python подчеркивает читабельность кода с заметным использованием значительных отступов. Его языковые конструкции и объектно-ориентированный подход призваны помочь программистам писать понятный, логичный код для небольших и масштабных проектов.

Python был создан в конце 1980-х годов Гвидо ван Россумом как преемник языка ABC. В версии Python 2.0, выпущенной в 2000 году, появились такие функции, как понимание списков и система сборки мусора, способная собирать циклы ссылок. Python 3.0, выпущенный в 2008 году, был серьезным пересмотром языка, который не является полностью обратно совместимым, и большая часть кода Python 2 не работает без изменений на Python 3.

Python - популярный язык для веб-разработки, научных вычислений, анализа данных, искусственного интеллекта и многого другого. Его стандартная библиотека обширна и включает модули для работы с базами данных, XML, электронной почтой, криптографией и многими другими задачами.
"""

# удаляем знаки препинания и приводим к нижнему регистру
words = re.findall(r'\w+', text.lower())

# подсчитываем количество повторений каждого слова
word_counts = Counter(words)

# выводим 10 самых частых слов
for word, count in word_counts.most_common(10):
    print(word, count)