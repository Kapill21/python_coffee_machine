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






def menu_info(which):
    wtr = MENU[which]['ingredients']['water']
    try:
        mlk = MENU[which]['ingredients']['milk']
    except KeyError:
        mlk = 0
    java = MENU[which]['ingredients']['coffee']
    price = MENU[which]['cost']

    return wtr, mlk, java, price




def check_resources(wtr,mlk,cfe):
    wtr = wtr
    mlk = mlk
    cfe = cfe

    if resources['water'] >= wtr:
        if resources['milk'] >= mlk:
            if resources['coffee'] >= cfe:
                resources['water'] -= wtr
                resources['milk'] -= mlk
                resources['coffee'] -= cfe
                return True

            else:
                print('Sorry, there is not enough coffee.')
                return False
        else:
            print('Sorry, there is not enough milk.')
            return False
    else:
        print('Sorry, there is not enough water.')
        return False




def enough_money(price):
    print('Please insert coins.')
    quarters = 0.25 * float(input('How many quarters: '))
    dimes = 0.10 * float(input('How many dimes: '))
    nickels = 0.05 * float(input('How many nickels: '))
    pennies = 0.01 * float(input('How many pennies: '))

    user_money = quarters + dimes + nickels + pennies
    if user_money >= float(price):
        change = float(user_money) - float(price)
        print(f'Here is ${change:.2f} in change.')
        global money
        money += cost
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False






money = 0
game_over = False
while not game_over:
    choice = input('What would you like? (espresso/latte/cappuccino): ')



    if choice == 'espresso':

        water, milk, coffee, cost = menu_info(choice)
        if enough_money(cost) and check_resources(water, milk, coffee):

            print(f'Here is your {choice}. Enjoy☕!')
        else:
            continue

    elif choice == 'latte':

        water, milk, coffee, cost = menu_info(choice)
        if enough_money(cost) and check_resources(water, milk, coffee):

            print(f'Here is your {choice}. Enjoy☕!')
        else:
            continue


    elif choice == 'cappuccino':

        water, milk, coffee, cost = menu_info(choice)
        if enough_money(cost) and check_resources(water, milk, coffee):

            print(f'Here is your {choice}. Enjoy☕!')
        else:
            continue



    elif choice == 'off':
        print()
        game_over = True



    elif choice == 'report':
        print(f'Water: {resources['water']}ml')
        print(f'Milk: {resources['milk']}ml')
        print(f'Coffee: {resources['coffee']}g')
        print(f'Money: {money}')
