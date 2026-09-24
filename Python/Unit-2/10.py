def cal(n):
    while n > 0:
        n -= 1
        yield n


for i in cal(10):
    print(i)