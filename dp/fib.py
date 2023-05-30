'''
f0 = 0
f1 = 1
fn = f n-1 + f n-2, for n > 1
'''

import time
from functools import lru_cache

n = 38
mem = [float("inf") for i in range(n + 1)]
mem[0] = 0
mem[1] = 1


# recursion
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# recursion with cache
@lru_cache()
def fib_cache(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)


# recursion with self defined mem
def fib_mem(n):
    # if n == 1 or n == 0:
    #     return 1
    # else:
    if mem[n] == float("inf"):
        mem[n] = fib_mem(n - 1) + fib_mem(n - 2)

    return mem[n]


# bottom up dp
def fib_dp(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    res = 0
    for i in range(2, n + 1):
        res = fib1 + fib2
        fib1 = fib2
        fib2 = res
    return res


if __name__ == "__main__":
    start_time = time.time()
    res = fib(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print("{:.8e}".format(execution_time))
    print()

    start_time = time.time()
    res = fib_cache(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print("{:.8e}".format(execution_time))
    print()

    start_time = time.time()
    res = fib_mem(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print(mem)
    print("{:.8e}".format(execution_time))
    print()

    start_time = time.time()
    res = fib_dp(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(res)
    print("{:.8e}".format(execution_time))
    print()


    test = [fib_dp(i) for i in range(n+1)]
    print(test)

