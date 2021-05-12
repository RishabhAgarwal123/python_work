from menu import MENU, resources

nextAction = True
# print(MENU)
# print(resources)

report = {
    'Water': resources['water'],
    'Milk': resources['milk'],
    'Coffee': resources['coffee'],
    'Money': 0
}


# def menu():
#     print("==========================MENU=======================")
#     print("Espresso :: $1.5")
#     print("Latte :: $2.5")
#     print("Cappuccino :: $3.0")


def manageReport(coffee):
    ingredients = coffee['ingredients']
    cost = coffee['cost']
    if report['Water'] >= ingredients['water']:
        report['Water'] = report['Water'] - ingredients['water']
        if coffee == 'latte' or coffee == 'cappuccino':
            report['Milk'] = report['Milk'] - ingredients['milk']
        report['Coffee'] = report['Coffee'] - ingredients['coffee']
        report['Money'] = report['Money'] + cost
        return True


def checkAvailability(coffee):
    isSufficient = False
    ingredients = coffee['ingredients']
    if report['Water'] >= ingredients['water'] and report['Coffee'] >= ingredients['coffee']:
        if coffee != 'espresso':
            if report['Milk'] >= ingredients['milk']:
                isSufficient = True
            else:
                print("Sorry there is not enough milk")
        else:
            isSufficient = True
    elif report['Water'] < ingredients['water']:
        print("Sorry there is not enough water")
    elif report['Coffee'] < ingredients['coffee']:
        print("Sorry there is not enough coffee")

# OR
#     for item in report:
#         if report[item] >= ingredients[item]:
#             print(f"Sorry there is not enough {item}")
#             isSufficient = False
    return isSufficient


def calculateMoney():
    pennies = int(input("Enter number of pennies : "))
    nickles = int(input("Enter number of nickles : "))
    dimes = int(input("Enter number of dimes : "))
    quarters = int(input("Enter number of quarters : "))
    dollars = (pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25)
    return dollars


def checkMoney(coffeePrice, customerMoney):
    if customerMoney >= coffeePrice:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


while nextAction:
    customerChoice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customerChoice == 'report':
        print(report)
    elif customerChoice == 'off':
        nextAction = False
    elif customerChoice == 'espresso' or customerChoice == 'latte' or customerChoice == 'cappuccino':
        print(MENU[customerChoice]['cost'])
        money = calculateMoney()
        available = checkAvailability(MENU[customerChoice])
        if not available:
            nextAction = False
        moneyStatus = checkMoney(MENU[customerChoice]['cost'], money)
        if available and moneyStatus:
            manageReport(MENU[customerChoice])
            change = money - MENU[customerChoice]['cost']
            if change > 0:
                print(f"Here is ${round(change, 3)} dollars in change. Here is your drink {customerChoice} enjoy.")
            else:
                print(f"Here is your drink {customerChoice} enjoy.")

# menu()
