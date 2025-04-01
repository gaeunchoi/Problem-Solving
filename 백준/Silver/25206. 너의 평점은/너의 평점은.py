# result에는 출력한 결과값을, total_credit에는 총학점을 저장한다.
total_grades = 0
total_credits = 0

ratings = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grades = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

for i in range(20):
    obj, credit, grade = input().split()
    if grade != 'P':
        total_credits += float(credit)
        total_grades += float(credit) * grades[ratings.index(grade)]

result = total_grades / total_credits
print("{:.6f}".format(result))
