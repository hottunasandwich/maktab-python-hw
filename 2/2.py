def is_prime(number):
    number = abs(number)
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False


for i in range(100):
    if is_prime(i):
        print(i, end=' ')
