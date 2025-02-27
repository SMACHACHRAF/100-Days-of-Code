MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    return all(resources[item] >= order_ingredients[item] for item in order_ingredients)


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid option. Please choose a valid drink.")


coffee_machine()
