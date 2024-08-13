# Использование %
print('В команде Мастера кода участников: %s' % 6)
print('В команде Волшебники данных участников: %s' % 6)
print('Итого сегодня в командах участников: %(team1)s и %(team2)s ' % {'team1': 6, 'team2': 6})

# Использование format()
print('Команда Мастера кода решила задач: {}'.format('40'))
print('Мастера кода решили задачи за {} c!'.format('1552.512'))
print('Команда Волшебники данных решила задач: {}'.format('42'))
print('Волшебники данных решили задачи за {} c!'.format('2153.31451'))


def score(arg):   # Использование f-строк
    date = []
    for i in arg:
        date.append(i)
    print(f'Команды решили {date[0]} и {date[1]} задач.')


team1_num = 6  # Мастера кода
team2_num = 6  # Волшебники данных

score1 = 40
score2 = 42
score_all = score([score1, score2])
print(f'Команды решили {score1 + score2} задач.')   # Использование f-строк

team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
print(f'Сегодня было решено {tasks_total} задач,'
      f'в среднем по {round((team1_time + team2_time) / tasks_total, 1)} секунды на задачу!')   # Использование f-строк

challenge_result = 'Победа команды Волшебники данных!'
print(f'Результат битвы: {challenge_result}')   # Использование f-строк

if score1 > score2 or score1 == score2 and team1_time < team2_time:
    result = f'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    result = f'Победа команды Волшебники Данных!'
else:
    result = f'Ничья!'
print(result)
