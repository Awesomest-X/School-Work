
def top_students(students_list):
    """
    Returns a tuple (top_names, top_score), where:
    - top_names is a list of student names who share the highest individual score
    - top_score is that score (or None if no scores)
    """
    top_score = None
    top_names = []
    for stu in students_list:
        if stu["scores"]:
            stu_max = max(stu["scores"])
            if top_score is None or stu_max > top_score:
                top_score = stu_max
                top_names = [stu["name"]]
            elif stu_max == top_score:
                top_names.append(stu["name"])
    return top_names, top_score
def find_student(students_list, name):
    """Return the student dict for `name`, or None if not found."""
    for student in students_list:
        if student["name"].lower() == name.lower():
            return student
    return None

def add_student(students_list, name):
    """Adds a new student with an empty score list."""
    students_list.append({"name": name, "scores": []})

def add_score(students_list, name, score):
    """Adds `score` to the specified student's scores."""
    student = find_student(students_list, name)
    if student:
        student["scores"].append(score)
        return True
    return False

def compute_statistics(scores_list):
    """Returns (average, highest, lowest) for a list of scores."""
    average = sum(scores_list) / len(scores_list)
    return average, max(scores_list), min(scores_list)

def grade_distribution(scores_list):
    """Returns counts of A/B/C/D/F for a list of scores."""
    dist = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for s in scores_list:
        if s >= 90: dist["A"] += 1
        elif s >= 80: dist["B"] += 1
        elif s >= 70: dist["C"] += 1
        elif s >= 60: dist["D"] += 1
        else: dist["F"] += 1
    return dist


def main():
    students = []

    while True:
        print("\n--- Grade Tracker Menu ---")
        print("1) Add a new student")
        print("2) Record a score for a student")
        print("3) Show a student's report")
        print("4) Show class report")
        print("5) Show all students")
        print("6) Exit")
        choice = input("Choose (1–6): ").strip()

        if choice == "1":
            name = input("Enter new student's name: ").strip()
            if find_student(students, name):
                print(f"Student '{name}' already exists.")
            else:
                add_student(students, name)
                print(f"Student '{name}' added.")

        elif choice == "2":
            name = input("Student name: ").strip()
            student = find_student(students, name)
            if not student:
                print(f"No student named '{name}'.")
                continue
            try:
                score = float(input("Enter score (0–100): "))
                if 0 <= score <= 100:
                    add_score(students, name, score)
                    print(f"Added score {score} for {name}.")
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score; please enter a number.")

        elif choice == "3":
            name = input("Student name for report: ").strip()
            student = find_student(students, name)
            if student and student["scores"]:
                avg, high, low = compute_statistics(student["scores"])
                dist = grade_distribution(student["scores"])
                print(f"\n--- Report for {student['name']} ---")
                print(f"Scores: {student['scores']}")
                print(f"Average: {avg:.2f}, High: {high}, Low: {low}")
                print("Grades:", ", ".join(f"{g}={c}" for g,c in dist.items()))
            elif student:
                print(f"{name} has no scores yet.")
            else:
                print(f"No student named '{name}'.")

        elif choice == "4":
            all_scores = [s for stu in students for s in stu["scores"]]
            if all_scores:
                avg, high, low = compute_statistics(all_scores)
                dist = grade_distribution(all_scores)
                tops, top_score = top_students(students)
                print("\n--- Class Report ---")
                print(f"Students tracked: {len(students)}")
                print(f"Total scores recorded: {len(all_scores)}")
                print(f"Average: {avg:.2f}, High: {high}, Low: {low}")
                print("Grades:", ", ".join(f"{g}={c}" for g,c in dist.items()))
                print(f"Top score {top_score} held by: {', '.join(tops)}")
            else:
                print("No scores recorded for any student.")

        elif choice == "5":
            if students:
                print("\n--- All Students ---")
                for stu in students:
                    print(f"• {stu['name']}")
            else:
                print("No students have been added yet.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice; please select 1–6.")

if __name__ == "__main__":
    main()
