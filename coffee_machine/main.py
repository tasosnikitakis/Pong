# global variables and dictionaries
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water_in_tank = resources["water"]
milk_in_tank = resources["milk"]
coffee_in_tank = resources["coffee"]
money_in_machine = 0
total = 0

# functions
def report_generation():
    print(f"Water: {water_in_tank}ml \nMilk: {milk_in_tank}ml \nCoffee: {coffee_in_tank}g \nMoney: ${money_in_machine}")


# sufficient resources check
def resources_check(user_choice):
    if user_choice == "espresso":
        user_choice_water = MENU[user_choice]["ingredients"]["water"]
        user_choice_coffee = MENU[user_choice]["ingredients"]["coffee"]
        water_check = water_in_tank - user_choice_water
        coffee_check = coffee_in_tank - user_choice_coffee
        if water_check < 0:
            print("Not enough water")
            return False
        elif coffee_check < 0:
            print("Not enough coffee")
            return False
        else:
            print("We are all good!")
            return True
    else:
        user_choice_water = MENU[user_choice]["ingredients"]["water"]
        user_choice_coffee = MENU[user_choice]["ingredients"]["coffee"]
        user_choice_milk = MENU[user_choice]["ingredients"]["milk"]
        water_check = water_in_tank - user_choice_water
        coffee_check = coffee_in_tank - user_choice_coffee
        milk_check = milk_in_tank - user_choice_milk
        if water_check < 0:
            print("Not enough water")
            return False
        elif coffee_check < 0:
            print("Not enough coffee")
            return False
        elif milk_check < 0:
            print("Not enough milk!")
            return False
        else:
            print("We are all good!")
            return True


# User money function
def user_money():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    cents = int(input("How many cents? "))
    user_total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (cents * 0.01)
    return user_total


# Check money function
def check_money(menu_item, coins_total):
    coffee_cost = MENU[menu_item]["cost"]
    if coins_total < coffee_cost:
        print(f"Sorry, you have ${coins_total} and the coffee costs ${coffee_cost}. That's not enough. Money refunded.")
    elif coins_total > coffee_cost:
        change = round(coins_total - coffee_cost, 2)
        print(
            f"You have inserted ${coins_total}, coffee costs ${coffee_cost}, here is your change: ${change}, thank you")
        return coffee_cost
    else:
        print("We are good to go")
        return coffee_cost


# TODO 2. Prompt User by asking "What would you like?"
# TODO 3. Turn off the coffe machine by entering "off" to the prompt
# TODO 4. Check for sufficient resources


def make_coffee():
    run_program = True
    while run_program:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        resources_check(user_choice)
        if not resources_check(user_choice):
            run_program = False
            make_coffee()
        else:
            # report code
            # TODO 1. Generate report of the coffee machine resources
            if user_choice == "report":
                report_generation()
            print("Please insert coins")
            user_money()
            check_money(user_choice, user_total)
            money_in_machine += MENU[user_choice]["cost"]
            print(f" money in coffee machine: {money_in_machine}")
            # Ingredients deduction
            if user_choice == "espresso":
                water_in_tank -= MENU[user_choice]["ingredients"]["water"]
                coffee_in_tank -= MENU[user_choice]["ingredients"]["coffee"]
            else:
                water_in_tank -= MENU[user_choice]["ingredients"]["water"]
                coffee_in_tank -= MENU[user_choice]["ingredients"]["coffee"]
                milk_in_tank -= MENU[user_choice]["ingredients"]["milk"]
            report_generation()
            print(f"Here is your {user_choice}, thank you very much!")


make_coffee()
