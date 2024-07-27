class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if int(new_floor) > int(self.number_of_floors) or int(new_floor) < 1:
            print(f'Такого этажа не существует')
        else:
            for i in range(0, int(new_floor)):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        if isinstance(other, int):
            return int(self.number_of_floors) == other
        # return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        if isinstance(other, int):
            return int(self.number_of_floors) < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        if isinstance(other, int):
            return int(self.number_of_floors) <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        if isinstance(other, int):
            return int(self.number_of_floors) > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        if isinstance(other, int):
            return int(self.number_of_floors) >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        if isinstance(other, int):
            return int(self.number_of_floors) != other

    def __add__(self, value):
        if isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        if isinstance(value, int):
            return House(self.name, int(self.number_of_floors) + value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
