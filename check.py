def fibonacci(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b

for x in fibonacci(10):
    print(x)


#teaching ameer hussain