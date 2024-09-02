def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        counter = 0
        if result > 1:
            for i in range(2, result // 2 + 1):
                if result % i == 0:
                    counter += 1
            if counter <= 0:
                print('Простое')
            else:
                print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_


result = sum_three(2, 3, 6)
print(result)
