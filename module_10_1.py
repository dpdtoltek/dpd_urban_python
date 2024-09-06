from threading import Thread
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        file = open(file_name, 'a', encoding='utf-8')
        file.write(f'Какое-то слово № {i}\n')
        sleep(0.1)
        file.close()
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
write1 = wite_words(10, 'example1.txt')
write2 = wite_words(30, 'example2.txt')
write3 = wite_words(200, 'example3.txt')
write4 = wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

time_start = datetime.now()
write5 = Thread(target=wite_words, args=(10, 'example5.txt'))
write6 = Thread(target=wite_words, args=(30, 'example6.txt'))
write7 = Thread(target=wite_words, args=(200, 'example7.txt'))
write8 = Thread(target=wite_words, args=(100, 'example8.txt'))

write5.start()
write6.start()
write7.start()
write8.start()
write5.join()
write6.join()
write7.join()
write8.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
