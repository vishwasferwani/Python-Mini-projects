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


def cost():

    quarters = int(input("how many quarters"))
    dimes = int(input("how many dimes"))
    nickles = int(input("how many nickles"))
    pennies = int(input("How many pennies"))
    coins = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return coins



def coffeemachine():
    again = True
    money = 0
    while again:
        user = input("welcome to coffee machine ☕\nWhat do you want ? :espresso/latte/cappuccino: ")

        if user == "report":
            print(resources)
            print(f"money:${money}")

        elif user == "off":

            return

        elif user == "espresso":

            if resources["water"] >= 50 and resources["coffee"] >= 18:
                customer_money = cost()
                if customer_money > 1.5:
                    print(f"enjoy your {user}")
                    change = round(customer_money - 1.5, 2)
                    print(f"here your change {change}")
                    money += 1.5
                    resources.update({"water": resources["water"] - 50})
                    resources.update({"coffee": resources["coffee"] - 18})

                else:
                    print("Not enough money, Money refunded")

            else:
                print("Not enough resources")

        elif user == "latte":

            if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
                customer_money = cost()
                if customer_money > 2.5:
                    print(f"enjoy your {user}")
                    change = round(customer_money - 2.5, 2)
                    print(f"here your change {change}")
                    money += 2.5
                    resources.update({"water": resources["water"] - 200})
                    resources.update({"coffee": resources["coffee"] - 24})
                    resources.update({"milk": resources["milk"] - 150})

                else:
                    print("Not enough money, Money refunded")

            else:
                print("Not enough resources")

        elif user == "cappuccino":

            if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
                customer_money = cost()
                if customer_money > 3:
                    print(f"enjoy your {user}")
                    change = round(customer_money - 3.0, 2)
                    print(f"here your change {change}")
                    money += 2.5
                    resources.update({"water": resources["water"] - 250})
                    resources.update({"coffee": resources["coffee"] - 24})
                    resources.update({"milk": resources["milk"] - 100})

                else:
                    print("Not enough money, Money refunded")

            else:
                print("Not enough resources")


coffeemachine()
