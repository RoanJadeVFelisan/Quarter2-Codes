num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))
print()

class_total = 0

for s in range(1, num_students + 1):
    print(f"Student {s}")
    student_total = 0

    for subj in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subj}: "))
        student_total += score

    student_average = student_total / num_subjects
    print(f"Average for Student {s} = {student_average}\n")

    class_total += student_average

class_average = class_total / num_students
print(f"Class Average = {class_average}")
