# import resources
def money_input():
    pennies = int(input("Pennies? ")) * 0.01
    nickles = int(input("nickles? ")) * 0.05
    dimes = int(input("dimes? ")) * 0.10
    quarter = int(input("quarter? ")) * 0.25

    return pennies + nickles + dimes + quarter

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
money_machine = 0.0

contd = True
while contd:
    user_choice = input("\n(espresso/latte/cappuccino): ").lower()
    if user_choice == 'e':
        user_choice = "espresso"
    elif user_choice == 'l':
        user_choice = "latte"
    elif user_choice == 'c':
        user_choice = "cappuccino"

    if user_choice == 'off':
        if input("Administrator Password : ") == 'kkr':
            contd = False
            # break
        else:
            print("Wrong Passcode...")
    elif user_choice == "refill":
        if input("Administrator Password : ") == 'kkr':
            print("how much to refill?")
            resources["water"] += int(input("water refill? "))
            resources["milk"] += int(input("milk refill? "))
            resources["coffee"] += int(input("coffee refill? "))
            # break
        else:
            print("Wrong Passcode...")
    elif user_choice == 'money':
        if input("Administrator Password : ") == 'kkr':
            money_machine -= int(input("how much money? "))
            # break
        else:
            print("Wrong Passcode...")
    elif user_choice == 'tip' or user_choice == 'donate':
        money_machine += money_input()
        print(f"thanks for {user_choice}")
    elif user_choice == 'report':
        print(
            f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money_machine}")
    elif MENU[user_choice]["ingredients"]["water"] < resources["water"] and MENU[user_choice]["ingredients"]["coffee"] < resources["coffee"] and MENU[user_choice]["ingredients"]["milk"] < resources["milk"]:
        # pennies = int(input("Pennies? ")) * 0.01
        # nickles = int(input("nickles? ")) * 0.05
        # dimes = int(input("dimes? ")) * 0.10
        # quarter = int(input("quarter? ")) * 0.25
        #
        # money_user = pennies + nickles + dimes + quarter
        # money_not_sufficient = "Sorry that's not enough money. Money refunded."
        money_user = money_input()

        if money_user < MENU[user_choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            print(f"the money difference between actual cost of {user_choice} and your given money is {MENU[user_choice]["cost"] - money_user}")
        else:
            # if MENU[user_choice]["ingredients"]["water"] < resources["water"] and MENU[user_choice]["ingredients"]["coffee"] < resources["coffee"] and MENU[user_choice]["ingredients"]["milk"] < resources["milk"]:
            resources["water"] -= MENU[user_choice]["ingredients"]["water"]
            resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
            money_machine += MENU[user_choice]["cost"]
            print(f"Remained money = ${round(money_user - MENU[user_choice]["cost"], 1)}")
            print(f"Enjoy {user_choice} ☕")
        # if user_choice == 'latte':
        #     if money_user < 2.5:
        #         print(money_not_sufficient)
        #         continue
        #     resources["water"] -= 200
        #     resources["milk"] -= 150
        #     resources["coffee"] -= 24
    else:
        # print("not enough resources")
        # if MENU[user_choice]["ingredients"]["water"] > resources["water"]:
        #     print("not enough water")
        for i in ["water", "coffee", "milk"]:
            if MENU[user_choice]["ingredients"][i] > resources[i]:
                print(f"not enough {i}, pls refill")
