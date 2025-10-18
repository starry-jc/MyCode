# Problem: ccc11s2

questions = int(input())
students = []
answers = []
correct = 0

for _ in range(questions):
    student = input()
    students.append(student)

for _ in range(questions):
    answer = input()
    answers.append(answer)
    
for i in range(questions):
    if students[i] == answers[i]:
        correct += 1

print(correct)