def average(values):
    return sum(values) / len(values)


n_students = int(input())
student_records = {}

for _ in range(n_students):
    name, grade_as_str = input().split()
    grade = float(grade_as_str)

    if name not in student_records:
        student_records[name] = []
    student_records[name].append(grade)

for name, grade in student_records.items():
    average_grade = average(grade)
    grades_str = ' '.join([str(f"{x:.2f}") for x in grade])
    print(f'{name} -> {grades_str} (avg: {average_grade:.2f})')

