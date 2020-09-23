string = input("Enter your string: ")
dic_chars = {} #make an empty dic

for char in string: #for every char in string 
    dic_chars.setdefault(char, 0)
    dic_chars[char] += 1
    
for key, value in dic_chars.items(): 
    print(f'({key}, {value})', end=' ') #print them in specified format
