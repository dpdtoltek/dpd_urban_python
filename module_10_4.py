from threading import Thread
from random import randint
import queue
from time import sleep


class Table:
    tables = {}
    guest = None

    def __init__(self, number):
        self.number = int(number)
        Table.tables[self.number] = Table.guest


class Guest(Thread):

    def __init__(self, name):
        super().__init__(daemon=None, args=(name, ))
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    q = queue.Queue()

    def __init__(self, *args):
        self.tables = [*args]

    def guest_arrival(self, *guests):
        self.guests = [*guests]
        for name in self.guests:
            self.q.put(name)
        for table in Table.tables:
            if Table.tables[table] is None:
                Table.guest = self.q.get()
                Table.tables[table] = Table.guest
                print(f'{Table.guest.name} сел(-а) за стол номер {table}')
                th = Guest(Table.guest)
                th.start()
                th.join()
        for i in self.q.queue:
            print(f'{i.name} в очереди')

    def discuss_guests(self):
        while not self.q.empty():
            for number, name in Table.tables.items():
                if name is not None and not Guest(name).is_alive():
                    print(f'{name.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {number} свободен')
                    Table.tables[number] = None
                    Table.guest = None
                    if not self.q.empty() and Table.guest is None:
                        Table.guest = self.q.get()
                        Table.tables[number] = Table.guest
                        print(f'{Table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {number}')
                        th = Guest(Table.guest)
                        th.start()
                        th.join()
        else:
            for number, name in Table.tables.items():
                if name is not None and not Guest(name).is_alive():
                    print(f'{name.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {number} свободен')
                    Table.tables[number] = None
                    Table.guest = None


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
# Проверка на наличие гостей за столами
print(Table.tables)
