# import resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
money = 0.0

contd = True
while contd:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        if input("Administrator Password : ") == 'kkr':
            contd = False
            # break
        else:
            print("Wrong Passcode...")
    elif user_choice == 'report':
        print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money}")
    else:
        pennies = int(input("Pennies? ")) * 0.01
        nickles = int(input("nickles? ")) * 0.05
        dimes = int(input("dimes? "))
        quarter = int(input("quarter? "))

        if user_choice == 'espresso' or user_choice == 'e':



