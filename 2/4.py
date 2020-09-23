def reverse(string):
    return string[::-1]

def is_palindrome(string):
    return string == reverse(string)

while True:
    string = input('Enter your text (palindrome checker): ')
    if is_palindrome(string):
        print('It\'s a palindrome!')
    else:
        print('It\'s not a palindrome!')
