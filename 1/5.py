counter = 0

#used excepting handling at its beginner level in order to make it look cool for no reason 
#actually to not make my application crash
try:
    n = int(input("Enter a non float number: "))
    
    #convert to string so its easier to calculate
    n = str(n)
    
    for digit in n:
        if digit in '0123456789':
            counter += 1
    print(counter)
except:
    print("You didnt enter a number or integer")
