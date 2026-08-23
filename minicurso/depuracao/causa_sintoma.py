scores = [85, 90, 78]
weights = [0.3, 0.4, 0.3]

total = 0

for i in range(len(scores)):
    total = total + scores[i] * weights[i]

print("Weighted total:", total)
print("Expected:", 85*0.3 + 90*0.4 + 78*0.3)


def get_student_data():
    students = []
    count = int(input("How many students? "))
    for i in range(count):
        print(f"\nStudent {i + 1}")
        name = input("Name: ")
        exam1 = float(input("Exam 1: "))
        exam2 = float(input("Exam 2: "))
        project = float(input("Project: "))
        students.append({
            "name": name,
            "scores": [exam1, exam2, project]
        })
    return students

def calculate_weighted_total(scores):
    weights = [0.3, 0.4, 0.3]
    total = 0
    for i in range(len(scores)):
        total = total + scores[i] * weights[i]
    return total

def display_results(students):
    print("\nResults")
    print("-" * 40)

    for student in students:
        total = calculate_weighted_total(student["scores"])

        if total >= 90:
            grade = "A"
        elif total >= 80:
            grade = "B"
        elif total >= 70:
            grade = "C"
        elif total >= 60:
            grade = "D"
        else:
            grade = "F"

        print(
            f"{student['name']:15} "
            f"Total={total:.2f} "
            f"Grade={grade}"
        )


def main():
    students = get_student_data()

    if len(students) == 0:
        print("No students entered.")
        return

    display_results(students)


main()


