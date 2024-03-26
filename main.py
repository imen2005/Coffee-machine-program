MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
def check_resources_sufficient(customer_order):
    """Checks if the ressources are sufficient for the order and returns the incompleted ingredient"""
    for ingredient in MENU[customer_order]["ingredients"]:
        if resources[ingredient] < MENU[customer_order]["ingredients"][ingredient]:
            return ingredient
    return ""

def print_report():
    """Prints the report"""
    print("I have the following resources:")
    for resource in resources:
        print(f"{resource}: {resources[resource]}", end='')
        if resource == "coffee":
            print("g")
        else:
            print("ml")
    print(f"money: ${money}")

def the_rest(customer_order):
    """Processes the coins inserted and returns the change"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return coins - MENU[customer_order]["cost"]

def make_the_drink(customer_order):
    """Makes the coffee and updates the ressources after an order"""
    global money
    money += MENU[customer_order]["cost"]
    for ingredient in MENU[customer_order]["ingredients"]:
        resources[ingredient] -= MENU[customer_order]["ingredients"][ingredient]


def order(customer_order):
    if check_resources_sufficient(customer_order) != "":
        print(f"Sorry there\'s not enough {check_resources_sufficient(customer_order)}")
    else:
        change = round(the_rest(customer_order), 2)
        if change < 0:
            print("Sorry that\'s not enough money. Money refund.")
        else:
            print(f"Here\'s ${change} in change.")
            print(f"Here\'s your {customer_order}. Enjoy!")
            make_the_drink(customer_order)
        
    
        
        
while True:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_order == "off":
        break
    elif customer_order == "report":
        print_report()
    else:
        order(customer_order)
