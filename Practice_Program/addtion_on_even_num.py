def my_fun(a):
    n = 0
    for _ in str(a):
        if a % 2 == 0:
            n += a

    print(n)
my_fun(10)