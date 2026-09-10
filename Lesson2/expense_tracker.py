#===== EXPENSE TRACKER =====#

def main():
    expense_tracker()


def expense_tracker():
    expenses = []
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total")
        print("4. Exit")   
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            expense = add_expense()
            expenses.append(expense)
            
        elif choice == 2:
            display_expenses(expenses)
            
        elif choice == 3:
            display_total(expenses)
            
        elif choice == 4:
            print("Have a nice day!!!")
            break
        else:
            print("Enter a valid number")

def add_expense():
    expense = int(input("Enter expense amount: "))
    return expense

def display_expenses(expenses):
    for i in range(len(expenses)):
        print(f"{i + 1}. {expenses[i]}")

def display_total(expenses):
    total = 0
    
    for expense in expenses:
        total += expense
    
    print(f"Total = {total}")


main()