input_str = '[1,2,[1,2,[1,2,[1],3,[1],[1,2,[1,4]]]]]'

def read_list(input_str):
    return eval(input_str)

def flatten(mylist, l=[]): # a recursive function 
    for element in mylist:
        if type(element) == list:
            flatten(element, l)
        else:
            l.append(element)
    return l

flattened_list = flatten(read_list(input_str))
print(flattened_list)
