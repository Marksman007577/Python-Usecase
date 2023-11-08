# Coffee Machine Project
from coffee_emoji import emoji

coffee_emoji = emoji

menu = {
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

resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

profit = 0


def check_resources(coffee_choice):
    """This function checks that there are available resources to make the coffee"""
    for item in coffee_choice:
        if coffee_choice[item] <= resources[item]:
            return True
        else:
            print(f"There is not enough {item}")
            return False


def process_coin():
    """This function processes the coin the user inputs"""
    print("Enter your coins here")
    total_pennies = float(input("How many pennies:"))*0.01
    total_nickles = float(input("How many nickles:")) * 0.05
    total_dimes = float(input("How many dimes:")) * 0.10
    total_quarters = float(input("How many quarters:")) * 0.25
    total_coins = round(total_pennies + total_nickles + total_dimes + total_quarters, 2)
    return total_coins


def successful_transaction(drink_cost,customer_payment):
    """This function checks if the right amount of coin was inserted for the chosen drink"""
    if customer_payment < drink_cost:
        print(f"Sorry that's not enough money. ${customer_payment} refunded.")
    elif customer_payment >= drink_cost:
        global profit
        balance = round(customer_payment - drink_cost, 2)
        profit += drink_cost
        print(f"Here is a balance of ${balance} in change")
        return True


def make_coffee(question, drink_choice):
    """This function perform the task of making the coffee"""
    for item in drink_choice:
        resources[item] -= drink_choice[item]
    print(f"Here is your {question} ☕.Enjoy!")


def coffee_machine():
    is_on = True
    while is_on:
        print(f"River Bear Coffee Machine{coffee_emoji}")

        prompt = input("What would you like? (espresso/latte/cappuccino):").lower()

        if prompt == "off":
            is_on = False

        elif prompt == "report":
            print(f"Water:{resources['water']}ml")
            print(f"Milk:{resources['milk']}ml")
            print(f"Coffee:{resources['coffee']}g")
            print(f"Money:${profit}")

        else:
            user_choice = menu[prompt]
            is_resource_sufficient = check_resources(user_choice['ingredients'])
            if is_resource_sufficient:
                payment = process_coin()
                correct_amount = successful_transaction(drink_cost=user_choice['cost'], customer_payment=payment)
                if correct_amount:
                    make_coffee(question=prompt, drink_choice=user_choice['ingredients'])


coffee_machine()
