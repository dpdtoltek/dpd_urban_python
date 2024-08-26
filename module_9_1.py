def apply_all_func(int_list, *functions):
    int_list = list(int(i) for i in int_list)
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


print(apply_all_func([6, '3', 20, 15, 9, True], max, min), end=' ')
print(apply_all_func([6, 20, 15, '22', 9, False], len, sum, sorted))
