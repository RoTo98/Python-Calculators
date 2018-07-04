def counter (n):
    if n == 1:
        return 1
    else:
        return n*counter(n-1)

