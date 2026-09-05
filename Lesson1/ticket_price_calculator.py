def main():
    calculate()

def calculate():
    age = int(input("Enter age: "))
    student = input("Are you a student: ").lower()
    
    
    original_price = get_ticket_price(age)
    discount = calculate_discount(original_price, student)
    final_price = original_price - discount
    
    display_summary(original_price, discount, final_price)
    

def get_ticket_price(age):
    
    if age < 12:
        price = 5
    elif age >= 12 and age <= 17:
        price = 8
    elif age >= 18 and age <= 59:
        price = 12
    elif age >= 60:
        price = 7

    return price

def calculate_discount(price, student):
    
    if student == "yes":
        discount = price * 0.2
        return discount
    else:
        return 0

def display_summary(price, discount, final_price):
    
    print(f"Original price: ${price:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final price: ${final_price:.2f}")
    

main()