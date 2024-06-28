def my_fun(s):
    r = 0
    for _ in str(s):
        r = r * 10 + (s % 10)
        s = s // 10
    print(r)
my_fun(12365)