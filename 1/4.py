def pos(n): #if the number is less than zero it makes it positive
    if n < 0:
        return -n
    else:
        return n
#takes the range and doesnt accept negative
minim = pos(int(input("enter first number: "))) 

maxim = pos(int(input("enter second number: ")))

#switches the positions in case the minimum is bigger than maximum
if minim > maxim:
    minim, maxim = maxim, minim

#a function that checks if the number is prime or not
def aval(a):
    if a == 1:
        return False
    for i in range(2, a // 2 + 1):  #it was better to use do-while since it had to check the number at least one time
        if a % i == 0:              #so we wouldnt have extra if on line 15
            return False
    return True

#checks the range for the first encountered prime
for i in range(minim+1, maxim):
    if aval(i):
        print(i)
        break
else:   #in case of not finding prime number
    print("No prime numbers found")
