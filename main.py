from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
isOn = True


while isOn:
    options = menu.get_items()
    userChoice = input(f"What would you like {options}").lower()
    if userChoice == 'off':
        isOn = False
    elif userChoice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(userChoice)
        enoughResources = coffeeMaker.is_resource_sufficient(drink)
        if enoughResources:
            success = moneyMachine.make_payment(drink.cost)
            if success:
                coffeeMaker.make_coffee(drink)