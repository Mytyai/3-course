class FibonacciLst:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0
        self.fib_set = self._generate_fib_up_to(max(self.instance))
    
    def _generate_fib_up_to(self, max_num):
        """Генерация чисел Фибоначчи до макс знач"""
        a, b = 0, 1
        fib_set = {a, b}
        while b <= max_num:
            a, b = b, a + b
            fib_set.add(b)
        return fib_set

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.instance):
            res = self.instance[self.idx]
            self.idx += 1
            if res in self.fib_set:
                return res
        raise StopIteration

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
fib_iterator = FibonacciLst(lst)
print(list(fib_iterator))  # [0, 1, 2, 3, 5, 8, 1]
