import math


class Figure:

    def __init__(self, color, *sides, sides_count=0):
        self.__color = list(color)
        self.sides = sides
        self.sides_count = sides_count
        self.__sides = []
        self.filled = True
        self.sides_list = []
        for i in self.sides:
            self.sides_list.append(i)
            if all(isinstance(s, int) and s > 0 for s in self.sides_list):
                if len(self.sides_list) == self.sides_count:
                    self.__sides = list(self.sides_list)
                elif len(self.sides_list) == 1:
                    self.__sides = self.sides_list * self.sides_count
                else:
                    self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        if 0 <= self.r <= 255 >= self.g >= 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
        if Figure.__is_valid_color(self, r, g, b) is True:
            self.__color[0:3] = [r, g, b]
        else:
            return

    def __is_valid_sides(self, *sides):
        # self.sides_count = sides_count
        self.sides = sides
        if (isinstance(self.sides, int) and self.sides > 0 and len(self.__sides) == self.sides_count
                or all(isinstance(s, int) and s > 0 for s in self.sides) and len(self.__sides) == self.sides_count):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        self.length = sum(Figure.get_sides(self))
        return self.length

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        self.new_sides_list = []
        for i in self.new_sides:
            self.new_sides_list.append(i)
        if Figure.__is_valid_sides(self, *new_sides) is True and len(self.new_sides) == self.sides_count:
            self.__sides = self.new_sides_list
        else:
            self.__sides = self.__sides


class Circle(Figure):
    def __init__(self, color, *sides, sides_count=1):
        super().__init__(color, *sides, sides_count=1)

        self.__radius = Figure.get_sides(self)[0] / 2 * math.pi

    def get_square(self):
        self.s = math.pi * math.pow(self.__radius)
        return self.s


class Triangle(Figure):
    def __init__(self, color, *sides, sides_count=3):
        super().__init__(color, *sides, sides_count=3)

    def get_square(self):
        self.a = Figure.get_sides(self)[0]
        self.b = Figure.get_sides(self)[1]
        self.c = Figure.get_sides(self)[2]
        self.p = (self.a + self.b + self.c) / 2
        self.s = math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
        return round(self.s, 2)


class Cube(Figure):
    def __init__(self, color, *sides, sides_count=12):
        super().__init__(color, *sides, sides_count=12)

    def get_volume(self):
        self.volume = Figure.get_sides(self)[0] ** 3
        return self.volume


circle1 = Circle((200, 200, 100), 10, 15, 6)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка треугольника
triangle1 = Triangle((25, 90, 150), 8, 15, 9)
print(triangle1.get_color())
print(triangle1.get_sides())
print(len(triangle1))
print(triangle1.get_square())
