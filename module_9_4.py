import random


class MysticBall:
    """Класс для случайного выбора слов."""

    def __init__(self, *words):
        self.words = words
        word = MysticBall.__call__(self)

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', 'Никогда')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*date_set):
        file = open(file_name, 'w', encoding='utf-8')
        # date = (i if isinstance(i, str) else str(i) for i in date_set)
        date = (i for i in date_set)
        for j in date:
            file.write(f'{j}\n')
        file.close()

    return write_everything


write = get_advanced_writer('exemple.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda i, j: i[:] == j[:], first, second)))
