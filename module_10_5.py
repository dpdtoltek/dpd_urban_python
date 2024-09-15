import multiprocessing
import os
from datetime import datetime

cur_dir = os.getcwd()


# 0:00:04.877472
def read_info(name):
    all_date = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if line:
                all_date.append(line)


# filenames = [f'./file {number}.txt' for number in range(1, 5)]
#
# time_start = datetime.now()
# for i in filenames:
#     read_info(i)
# time_end = datetime.now()
# print(time_end - time_start)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        time_start = datetime.now()
        pool.map(read_info, filenames)
    time_end = datetime.now()
    print(time_end - time_start)
