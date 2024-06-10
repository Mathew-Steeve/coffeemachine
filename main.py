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

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def coffee_choice():

    choice = input("What do you like?(espresso/latte/cappuccino)")
    if choice == "report":

        print(f"water:{resource['water']}ml")
        print(f"milk:{resource['milk']}ml")
        print(f"coffee:{resource['coffee']}g")
        print(f"Money:${money}")
        coffee_choice()

    elif choice == "off":
        exit()

    else:
        coffee_making(choice)


def cost_evaluation():

    print("Please insert coin.")
    total = int(input("How many quarters ?"))*0.25
    total += int(input("How many dimes ?"))*0.1
    total += int(input("How many nickels ?"))*0.05
    total += int(input("How many pennies ?"))*0.01

    return total


def coffee_making(choice):

    for item in MENU:
        if choice == item:

            check_resource(choice)
            add = cost_evaluation()
            # resource[item] = resource.get(item)-MENU[choice]["ingredients"]
            real_cost = MENU[choice]["cost"]
            if add > real_cost:
                result = add - real_cost
                print(f"Here is your change ${round(result, 2)}")
                print(f"Here is your {choice}.☕ enjoy")

            else:
                print("Sorry that is not enough money. Money refunded.")
    for item in MENU[choice]["ingredients"]:
        resource[item] -= MENU[choice]["ingredients"][item]
    global money
    money += MENU[choice]["cost"]
    coffee_choice()


def check_resource(x):
    insufficient_resources = []
    for item in MENU[x]["ingredients"]:
        if MENU[x]["ingredients"][item] > resource[item]:
            insufficient_resources.append(item)

    if insufficient_resources:
        print(f"Sorry, not enough resources: {', '.join(insufficient_resources)}")
        coffee_choice()


coffee_choice()
