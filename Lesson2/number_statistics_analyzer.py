def main():
    number_analyzer()
    
def number_analyzer():
    numbers = []
    
    while True:
        print("\n===== Number Statistics Analyzer =====")
        print("1. Add number")
        print("2. View all numbers")
        print("3. Calculate highest number")
        print("4. Calculate lowest number")
        print("5. Calculate positive number count")
        print("6. Calculate negative number count")
        print("7. Calculate even number count")
        print("8. Calculate odd number count")
        print("9. Calculate total of numbers")
        print("10. Calculate average of numbers")
        print("11. Exit")   
        
        choice = int(input("Enter a Choice: "))
        
        if choice == 1:
            number = add_number()
            numbers.append(number)
        elif choice == 2:
            display_numbers(numbers)
        elif choice == 3:
            highest_number(numbers)
        elif choice == 4:
            lowest_number(numbers)
        elif choice == 5:
            positive_count(numbers)
        elif choice == 6:
            negative_count(numbers)
        elif choice == 7:
            even_count(numbers)
        elif choice == 8:
            odd_count(numbers)
        elif choice == 9:
            calc_total(numbers)
        elif choice == 10:
            calc_avg(numbers)
        elif choice == 11:
            print("Have a nice day!!!")
            break
        else:
            print("Enter a valid choice")

def add_number():
    number = int(input("Enter a number: "))
    return number

def display_numbers(numbers):
    for i in range(len(numbers)):
        print(f"{i + 1}. {numbers[i]}")
    
def highest_number(numbers):
    
    if len(numbers) == 0:
        print("No numbers have been added yet.")
        return

    highest = numbers[0]
    
    for number in numbers:
        if number > highest:
            highest = number
            
    print(f"Highest number = {highest}")

def lowest_number(numbers):
    
    if len(numbers) == 0:
        print("No numbers have been added yet.")
        return
    
    lowest = numbers[0]
    
    for number in numbers:
        if number < lowest:
            lowest = number
    print(f"Lowest number = {lowest}")

def positive_count(numbers):
    count_positive_numbers = 0
    for number in numbers:
        if number > 0:
            count_positive_numbers += 1
    
    print(f"Positive number count= {count_positive_numbers}")


def negative_count(numbers):
    count_negative_numbers = 0
    for number in numbers:
        if number < 0:
            count_negative_numbers += 1
    
    print(f"Negative number count= {count_negative_numbers}")
    
def even_count(numbers):
    count_even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            count_even_numbers += 1
    print(f"Even number count = {count_even_numbers}")
    
def odd_count(numbers):
    count_odd_numbers = 0
    for number in numbers:
        if number % 2 != 0:
            count_odd_numbers += 1
    print(f"Odd number count = {count_odd_numbers}")
    
def calc_total(numbers):
    total = 0
    for number in numbers:
        total += number
    print(f"Total = {total}")
    
def calc_avg(numbers):
    if len(numbers) == 0:
        print("No numbers have been added yet.")
        return

    total = 0
    count = 0

    for number in numbers:
        count += 1
        total += number

    average = total / count

    print(f"Average = {average}")
    
main()