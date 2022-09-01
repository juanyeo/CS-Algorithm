n = int(input())

students = []

for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students = sorted(students, key= lambda x: x[1])

for student in students:
    print(student[0])
