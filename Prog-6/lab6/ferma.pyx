from libc.math cimport sqrt
cdef inline int isqrt(unsigned long long n):
    return <int>sqrt(n)

cpdef bint is_perfect_square(unsigned long long n):
    cdef int root = isqrt(n)
    return root * root == n

cpdef tuple fermat_factorization(unsigned long long N):
    cdef unsigned long long x, y_squared, y
    if N % 2 == 0:
        return 2, N // 2

    x = isqrt(N) + 1
    while True:
        y_squared = x * x - N
        if is_perfect_square(y_squared):
            y = isqrt(y_squared)
            return (x - y, x + y)
        x += 1
