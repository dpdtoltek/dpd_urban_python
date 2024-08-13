import io
from pprint import pprint


class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                line = file.read().replace('\n', ' ')
                line = line.lower()
                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for p in punctuation:
                    if p in line:
                        line = line.replace(p, '')
                line = line.split()
                all_words[name] = line
        return all_words

    def find(self, word):
        find_word = {}
        for name, words in finder2.get_all_words().items():
            if word.lower() in words:
                find_word[name] = words.index(word.lower()) + 1
            else:
                find_word[name] = f'слово {word} отсутствует'
        return find_word

    def count(self, word):
        count_word = {}
        for name, words in finder2.get_all_words().items():
            if word.lower() in words:
                count_word[name] = words.count(word.lower())
            else:
                count_word[name] = f'слово {word} отсутствует'
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
