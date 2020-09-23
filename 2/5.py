'''
this is a 2 in 1, what it does is that it chooses the first letter of each sentece 
and adds to first letter variable and at the end prints the letters
'''
allowed_chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
def sentence_spliter(sentence):
    first_letters = ''
    ready_to_catch_word = True
    for letter in sentence:
        if letter.lower() in allowed_chars and ready_to_catch_word == True:
            first_letters += letter.upper()
            ready_to_catch_word = False
        elif letter.lower() not in allowed_chars and ready_to_catch_word == False:
            ready_to_catch_word = True
    return first_letters
'''
a word selector that seperates words in sentece and returns a list of 
that words
'''
def word_selector(sentence):
    word_list = []
    word = ''
    for letter in sentence:
        if letter.lower() in allowed_chars:
            word += letter
        else:
            if len(word):
                word_list.append(word)
            word = ''
    if len(word):
        word_list.append(word)
    return word_list
'''
first letter capitalizer function that gets a list of words and capitalizes the
fist letter joins them and returns a string 
'''
def fl_capitalizer(words):
    res = ''
    for i in words:
        res += i[0].upper()
    return res

while True:
    sentence = input('Enter your sentence(s): ')

    print('output 1: {}'.format(sentence_spliter(sentence)))
    print('output 2: {}'.format(fl_capitalizer(word_selector(sentence))))
