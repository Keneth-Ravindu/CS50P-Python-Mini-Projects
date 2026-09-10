#===== EXPENSE TRACKER =====#

def main():
    expense_tracker()


def expense_tracker():
    total = 0
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View total")
        print("3. Exit")   
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            total += add_expense()
            
        elif choice == 2:
            display_total(total)
            
        elif choice == 3:
            print("Have a nice day!!!")
            break
        else:
            print("Enter a valid number")

def add_expense():
    expense = int(input("Enter expense amount: "))
    return expense


def display_total(total):
    print(f"Total = {total}")
    
        
main()