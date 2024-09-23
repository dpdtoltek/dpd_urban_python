from pprint import pprint
import requests
import pandas as pd
import numpy as np


# Библиотека requests
r = requests.get('https://docs.python.org')
print(r.ok)
print(r.status_code)
headers = r.headers
for key, value in headers.items():
    pprint(f'{key}: {value}')
print('')

# Библиотека pandas
data1 = ['А', 'Б', 'В', 'Г', 'Д']
s = pd.Series(data1)
print(s)
print('')

data2 = {
    'Name': ['Anna', 'Maria', 'Daniil', 'Nikolai', 'Olga'],
    'Age': [25, 30, 35, 39, 21],
    'City': ['Moscow', 'Saint Petersburg', 'Penza', 'Kazan', 'Sochi'],
    'Average score': [4.8, 4.9, 3.9, 4.3, 4.5]
}

df = pd.DataFrame(data2)
df.to_csv('list of students', index=False)

df = pd.read_csv('list of students')
print(df.head())
print('')
print(df['Name'])
print('')
print(df.loc[1])
print('')
print(f'Минимальный возраст: {df['Age'].min()}')
print(f'Максимальный средний бал: {df['Average score'].max()}')
print('')

#Библиотека NumPy
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
pprint(a)
b = np.random.randint(1, 20, size=(2, 2, 3))
pprint(b)
pprint(a.ndim)
pprint(a.shape)
pprint(a.dtype)
pprint(a.size)
pprint(a[1, 1, 1])
pprint(a + 5)
pprint(a - 3)
pprint(a * 2)
pprint(a / 2)
pprint(a ** 2)
pprint(a + b)
pprint(f'Сумма всех элементов массива "a" = {a.sum()}')
mean_all_a = a.mean()
print(f'Среднее арифметическое всех элементов массива "a" = {mean_all_a}')
min_all_a = a.min()
print(f'Минимальное значение среди всех элементов массива "a" = {min_all_a}')
max_all_a = a.max()
print(f'Максимальное значение среди всех элементов массива "a" = {max_all_a}')
prod_all = a.prod()
print(f'Произведение всех элементов массива "a" = {prod_all}')
