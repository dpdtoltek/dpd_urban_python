class Vehicle:
    __COLOR_VARIANTS = ['black', 'orange ', 'white', 'yellow', 'gray']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        return f'Модель {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        new_color_ = str(new_color.lower())

        if new_color_ in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['black', 'orange ', 'white', 'yellow', 'gray']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Purple')
vehicle1.set_color('GRAY')
vehicle1.owner = 'Victor'

# Проверяем что поменялось
vehicle1.print_info()
