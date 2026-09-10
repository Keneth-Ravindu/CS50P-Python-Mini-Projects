def main():
    workout_tracker()
    
def workout_tracker():
    exercise_count= int(input("How many exercises? "))
    workout_total_reps = 0
    
    for i in range(exercise_count):
        exercise = input(f"Enter Exercise {i + 1}: ")
        
        
        set_count = int(input("How many sets? "))
        total_reps = 0
        avg_reps = 0
        
        for j in range(set_count):
            reps = int(input(f"Enter reps for set {j + 1}: "))         
            total_reps += reps
            workout_total_reps += total_reps
        
        avg_reps = total_reps/set_count
            
        print(f"Total reps for {exercise}: {total_reps}")
        print(f"Average reps per set {avg_reps}")
    
    print(f"Total reps for entire workout: {workout_total_reps}")
        
        
        

main()