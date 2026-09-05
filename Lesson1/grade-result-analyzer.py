def main():
    decision()


def decision():
    mark = float(input("Enter mark: "))

    grade = get_grade(mark)
    feedback = get_feedback(grade)

    get_performance(mark, grade, feedback)


def get_grade(mark):

    if mark >= 85 and mark <= 100:
        return "A+"

    elif mark >= 75:
        return "A"

    elif mark >= 65:
        return "B"

    elif mark >= 55:
        return "C"

    elif mark >= 40:
        return "D"

    elif mark >= 0:
        return "F"


def get_feedback(grade):

    if grade == "A+":
        return "Perfect"

    elif grade == "A":
        return "Best"

    elif grade == "B":
        return "Better"

    elif grade == "C":
        return "Good"

    elif grade == "D":
        return "Not enough"

    elif grade == "F":
        return "Maybe next time"


def get_performance(mark, grade, feedback):
    print(f"Mark: {mark}")
    print(f"Grade: {grade}")
    print(f"Performance: {feedback}")


main()