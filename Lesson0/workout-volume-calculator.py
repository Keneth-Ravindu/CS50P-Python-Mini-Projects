####### Workout Volume Calculator #######

def main():
    exercise_log()


def exercise_log():
    exercise = input("Enter exercise: ")
    weight = float(input("Enter weight: "))
    reps = int(input("Enter reps: "))
    sets = int(input("Enter sets: "))

    display_summary(exercise, weight, reps, sets)


def get_exercise(e):
    return e


def calculate_volume(a, b):
    volume = a * b
    return volume


def calculate_total_volume(a, b, c):
    total_volume = a * b * c
    return total_volume


def display_summary(exercise, weight, reps, sets):
    print(f"\nExercise: {get_exercise(exercise)}")
    print(f"Volume per set: {calculate_volume(weight, reps)} kg")
    print(f"Total volume: {calculate_total_volume(weight, reps, sets)} kg")


main()