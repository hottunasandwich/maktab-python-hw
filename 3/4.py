class_one = [student for student in input().split(',')]
class_two = [student for student in input().split(',')]

print(set(class_one + class_two))
print([student for student in class_one if student in class_two])
print([student for student in class_one if student not in class_two])
print([student for student in class_two if student not in class_one])
print([student for student in class_one if student in class_two])
print(len(''.join([student for student in class_one if student in class_two])))
print([student for student in set(class_one + class_two) if len(student) > 10])
print(sorted([student for student in class_one if student not in class_two]))
