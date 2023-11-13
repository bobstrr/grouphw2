n = int(input())


students = {}


for i in range(n):
    input_data = input().split()
    name = input_data[0]
    grade = float(input_data[1])

    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = " ".join(map(str, grades))
    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
