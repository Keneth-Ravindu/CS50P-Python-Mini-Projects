def main():
    membership()


def membership():
    age = int(input("Enter age: "))
    student_status = input("Are you a student: ").lower()
    member_decision = input("Do you want a premium membership: ").lower()

    price = base_price(age)
    discount = student_discount(price, student_status)
    premium_membership = type_of_membership(member_decision)

    final_price = price - discount + premium_membership

    summary(price, discount, premium_membership, final_price)


def base_price(age):
    if age < 18:
        return 15

    elif age < 25:
        return 25

    elif age < 60:
        return 35

    else:
        return 20


def student_discount(price, student_status):
    if student_status == "yes":
        return price * 0.1
    else:
        return 0


def type_of_membership(member_decision):
    if member_decision == "yes":
        return 15
    else:
        return 0


def summary(price, discount, premium_membership, final_price):
    print(f"Base price: ${price:.2f}")
    print(f"Student discount: ${discount:.2f}")
    print(f"Premium charge: ${premium_membership:.2f}")
    print(f"Final price: ${final_price:.2f}")


main()