# Coffee machine program

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


money = {
    "amount": 0.0
}


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there's not enough {ingredient}")
            return False
        else:
            return True

def process_coins(drink):
    total = 0
    print("Please insert coins.")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")
    total += (float(quarters)*0.25) + (float(dimes)*0.1) + (float(nickles)*0.05) + (float(pennies) * 0.01)
    if total > MENU[drink]["cost"]:
        change = total - MENU[drink]["cost"]
        print(f"Here is ${change:.2f} in change")
        for ingredient in MENU[drink]["ingredients"]:
            resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
        print(f"Here is your {drink}. Enjoy!")
        money["amount"] += MENU[drink]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def coffee_machine():
    off = False
    while off == False:
        request = input("What would you like? (espresso/latte/cappuccino):")
        if request == "off":
            print("Coffee machine is now turned off")
            off = True
        elif request == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}ml")
            print(f"Money: ${money['amount']}")
        elif request in ["espresso", "latte", "cappuccino"]:
            if check_resources(request):
                process_coins(request)
        else:
            print("This is not a valid option. Please try again.")

coffee_machine()
