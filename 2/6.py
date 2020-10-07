import random
from math import ceil, floor

special_chars = '+-/*&^%#@!?.,\\|:\'"_~'
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()
numbers = '1234567890'

def special(n=1):
    return random.sample(special_chars, n)
def number(n=1):
    return random.sample(numbers, n)
def lower_letter(n):
    return random.sample(alphabet_lower, n)
def upper_letter(n=2):
    return random.sample(alphabet_upper, n)

def generate_password(n = floor(random.uniform(1, 2) * 10)):
    rand = random.randrange(1, 3)
    password = special(rand + 1) + upper_letter(rand + 2) + number(rand + 1) + lower_letter(n - 3 * rand - 4)
    random.shuffle(password)
    return ''.join(password)

print('password: {}'.format(generate_password()))

for k, v in list(globals().items()):
    print(k, '\t\t\t',v)

upper_letter(2)