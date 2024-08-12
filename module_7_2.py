import io
from pprint import pprint


def custom_write(file_name, strings):
    name = file_name
    # strings_list = strings
    strings_positions = {}
    file = open(name, 'w', encoding='utf-8')
    for i in range(1, len(strings)+1):
        k = file.tell()
        strings_positions[i, k] = strings[i-1]
        file.write(f'{strings[i-1]}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
