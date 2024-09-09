import threading
from threading import Thread, Lock
from time import sleep
from random import randint


class Bank(Thread):
    balance = int(0)
    lock = Lock()

    def __init__(self):
        super().__init__()
        self.trans_deposit = 100
        self.trans_take = 100

    def deposit(self):
        while self.trans_deposit > 0:
            deposit_ = randint(50, 500)
            bk.balance += deposit_
            self.trans_deposit -= 1
            print(f'Пополнение: {deposit_}. Баланс: {bk.balance}. ')
            if bk.balance >= 500 and bk.lock.locked():
                bk.lock.release()
            sleep(0.001)

    def take(self):
        while self.trans_take > 0:
            take_ = randint(50, 500)
            print(f'Запрос на {take_}. ')
            if take_ <= bk.balance:
                bk.balance -= take_
                self.trans_take -= 1
                print(f'Снятие: {take_}. Баланс: {bk.balance}. ')
            else:
                print('Запрос отклонён, недостаточно средств. ')
                bk.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}.')
