import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def my_genn():
    """Сопрограмма"""
    g = fib_elem_gen()
    fib_list = []
    
    while True:
        number_of_fib_elem = yield fib_list
        if number_of_fib_elem == 0:
            fib_list = []
        else:
            for _ in range(number_of_fib_elem - len(fib_list)):
                fib_list.append(next(g))

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    return inner

my_genn = fib_coroutine(my_genn)

gen = my_genn()

#print(gen.send(3))  # [0, 1, 1]
#print(gen.send(5))  # [0, 1, 1, 2, 3]
#print(gen.send(8))  # [0, 1, 1, 2, 3, 5, 8, 13]
