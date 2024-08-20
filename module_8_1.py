def add_everything_up(a, b):
    try:
        sum_1 = a + b
        return round(sum_1, 3)
    except TypeError:
        if type(a) is not type(b):
            a = str(a)
            b = str(b)
            sum_2 = a + b
            return sum_2


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
