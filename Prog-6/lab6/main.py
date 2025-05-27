import pyximport
pyximport.install(language_level=3)

import timeit
import matplotlib.pyplot as plt
from ferma import fermat_factorization as cython_fermat

# --- Python реализация
def is_perfect_square_py(n):
    root = int(n**0.5)
    return root * root == n

def fermat_factorization_py(N):
    if N % 2 == 0:
        return 2, N // 2
    x = int(N**0.5) + 1
    while True:
        y_squared = x * x - N
        if is_perfect_square_py(y_squared):
            y = int(y_squared**0.5)
            return (x - y, x + y)
        x += 1

# --- Тестируемые данные
TEST_LST = [101, 9973, 104729, 101909, 609133, 1300039, 9999991,
            99999959, 99999971, 3000009, 700000133, 61335395416403926747]

# --- Время Python
py_time = timeit.timeit(
    stmt='[fermat_factorization_py(i) for i in TEST_LST]',
    setup='from __main__ import fermat_factorization_py, TEST_LST',
    number=10
)

# --- Время Cython
cy_time = timeit.timeit(
    stmt='[cython_fermat(i) for i in TEST_LST]',
    setup='from __main__ import cython_fermat, TEST_LST',
    number=10
)

# --- График
labels = ['Python', 'Cython']
times = [py_time, cy_time]

plt.figure(figsize=(8, 5))
bars = plt.bar(labels, times, color=['tomato', 'mediumseagreen'])
plt.title("Сравнение времени выполнения\nМетод Ферма (10 повторений)")
plt.ylabel("Время (сек)")
plt.grid(axis='y')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{height:.2f}s', ha='center', va='bottom')

plt.tight_layout()
plt.show()