import math
lloyd = {
        'field': 'Computer',
        'homework': [90.0, 97.0, 75.0, 92.0],
        'quizzes': [88.0, 40.0, 94.0],
        'tests': [75.0, 90.0]
        }
alice = {
        'field': 'Civil',
        'homework': [100.0, 92.0, 98.0, 100.0],
        'quizzes': [82.0, 83.0, 91.0],
        'tests': [89.0, 97.0]
        }
tyler = {
        'field': 'Mechanics',
        'homework': [0.0, 87.0, 75.0, 22.0],
        'quizzes': [0.0, 75.0, 78.0],
        'tests': [100.0, 100.0]
        }

students = {'lloyd': lloyd, 'alice': alice, 'tyler': tyler}

def get_data(key):
    new_dic = {}
    for student in students:
        new_dic[student] = students[student][key]
    return new_dic

def get_averages(key = 'homework'):
    new_dic = {}
    for student in students:
        new_dic[student] = math.fsum(students[student][key]) / len(students[student][key])
    return new_dic

def get_class_average(key = 'homework', names = None):
    stu = get_averages(key)
    summit = 0

    if names != None:
        for name in names:
            summit += stu[name]
        avg = summit / len(names)
    else:
        avg = math.fsum(stu.values()) / len(stu)

    return avg

print(get_class_average('tests'))
