n = int(input())
mid = (n+1) // 2

for i in range(1, n+1):
    if i < mid:
        d = i
    else:
        d = 2 * mid - i

    for j in range(d):
        print('*', end='')
    print()
