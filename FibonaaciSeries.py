
# A method that print fibonaaci series.
def fibonaaci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        temp = a
        a = b
        b = temp + b

