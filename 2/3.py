def choose(n, k):
    if (k == 0 or n == k) and n >= 0:
        return 1
    elif n == 0:
        return 0
    else:
        return choose(n - 1, k - 1) + choose(n - 1, k)

def factor(number):
    if number == 0:
        return 1
    elif number < 0:
        raise ValueError("only natural numbers are acceptable!")
    else:
        return factor(number - 1) * number

def func_choose(n, k):
    if n < k and n >= 0 and k > 0:
        return 0
    else:
        return factor(n) // (factor(n - k) * factor(k))

while True:
    n, k = input('Enter n and k with a seperating space: ').split(' ')

    n = int(n)
    k = int(k)
    print('output formula: {}'.format(func_choose(n, k)))
    print('output recursive function: {}'.format(choose(n, k)))
