def main():
    shipping()


def shipping():
    package_weight = float(input("Enter package weight in kg: "))
    type_of_customer = input("Are you a premium customer? ").lower()
    type_of_delivery = input("Is this an express delivery? ").lower()

    total = get_base_cost(package_weight)
    discount = get_discount(type_of_customer, total)
    express_charge = get_express_charge(type_of_delivery)

    final_shipping_cost = total - discount + express_charge

    summary(total, discount, express_charge, final_shipping_cost)


def get_base_cost(package_weight):
    if package_weight <= 2:
        return 5

    elif package_weight <= 5:
        return 8

    elif package_weight <= 10:
        return 12

    else:
        return 20


def get_discount(type_of_customer, price):
    if type_of_customer == "yes":
        return price * 0.15
    else:
        return 0


def get_express_charge(type_of_delivery):
    if type_of_delivery == "yes":
        return 10
    else:
        return 0


def summary(total, discount, express_charge, final_shipping_cost):
    print(f"Base shipping cost = ${total:.2f}")
    print(f"Premium discount = ${discount:.2f}")
    print(f"Express charge = ${express_charge:.2f}")
    print(f"Final shipping cost = ${final_shipping_cost:.2f}")


main()