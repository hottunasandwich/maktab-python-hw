#easy question and simple answer
n = int(input())

if n >= 0 and n < 10:
    print("failed")

elif n >= 10 and n < 15:
    print("not bad")

elif n < 18 and n >= 15:
    print("good")

elif n >= 18 and n <= 20:
    print("excellent")

else:
    print("number not in range")

