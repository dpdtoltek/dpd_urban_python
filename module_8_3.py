class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.vin_number = vin_number
        self.numbers = numbers
        __vin = None
        __numbers = None
        if Car.__is_valid_vin(self, self.vin_number) is True:
            __vin = self.vin_number
        if Car.__is_valid_numbers(self, self.numbers) is True:
            __numbers = self.numbers

    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if not isinstance(self.vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if self.vin_number < 1000000 or self.vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.numbers = numbers
        if not isinstance(self.numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(self.numbers) < 6 or len(self.numbers) > 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
