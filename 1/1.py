#a recursive function
def factor(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 'UNACCEPTABLE'
    else:
        return n * factor(n-1)

#runs for ever and takes number to return its fact
while True:
    n = int(input("Enter n: "))
    print(factor(n))

