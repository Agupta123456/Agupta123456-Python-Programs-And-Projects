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

def sufficient_amt(order_ingredients):
    """Check resources are enough or not"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return  True


def amt_required():
    """Return the total amount"""
    print("Insert the coins.")
    Total = int(input("How many quarters? ")) * 0.25
    Total += int(input("How many dimes? ")) * 0.1
    Total += int(input("How many nickles? ")) * 0.05
    Total += int(input("How many pennies? ")) * 0.01

    return Total


def successful_transaction(money_received, drink_cost):
    """Return True when payment successful and False when money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit =+ drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        print(f"Here is Your {drink_name}.")
        break

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"fWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if sufficient_amt(drink["ingredients"]):
            payment = amt_required()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])

