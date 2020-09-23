'''
this program calculates numbers that 'number%100 == 0'
'''
#positive exchanger function
def positive(number):
    if number < 0:
        return -number
    else:
        return number

#bills that we have in our pocket
bills = [1000, 500, 200, 100]

cash = positive(int(input())) // 100 * 100

res = ''

for i in bills:
    counter = cash // i
    cash = cash % i

    if counter != 0:
        if res != '':
            res += ', '

        if (cash != 0 and i != len(bills) - 1) or res == '':
            res += '{} ({} bill)'.format(counter, i)
        else:
            res += 'and {} ({} bill)'.format(counter, i)

print(res)

