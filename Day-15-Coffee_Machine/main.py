from data import MENU, resources

def coins():
    '''Essa função armazena o input do usuário 
    com o valor das moedas que ele tem disponível
    e retorna a soma total das moedas'''

    print('Please insert coins')
    q = float(input('How many quarters? ')) * 0.25
    d = float(input('How many dimes? ')) * 0.10
    n = float(input('How many nickes? ')) * 0.05
    p = float(input('How many pennies? ')) * 0.01
    
    total = q + d + n + p 
    return total

def check_resources(drink):
    '''Essa função checa se a máquina tem recursos 
    o suficiente para fazer a bebida. Se sim, a função coins()
    é chamada, pedindo para o usuário inserir a quantidade de 
    moedas e posteriormente é usada a função transaction(). 
    Caso a máquina não tenha recursos, é retornada uma mensagem avisando da falta de ingredientes.'''

    if MENU[drink]['ingredients']['water'] > resources['water']:
        print('Sorry there is not enough water.')
    elif MENU[drink]['ingredients']['milk'] > resources['milk']:
        print('Sorry there is not enough milk.')
    elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry there is not enough coffee.')
    else:
        user_money = coins()
        transaction(user_money, drink)

def decrease_ingredients(drink_type):
    '''Diminui a quantidade de ingredientes caso a máquina tenha
    ingredientes o suficiente para fazer a bebida do usuário'''

    resources['water'] -= MENU[drink_type][ 'ingredients']['water']
    resources['milk'] -= MENU[drink_type][ 'ingredients']['milk']
    resources['coffee'] -= MENU[drink_type][ 'ingredients']['coffee']
    

def transaction(user_founds, drink_choose):
    '''Checa se o usuário tem dinheiro o suficiente para pagar pela bebida.
    user_founds é a soma total das moedas
    drink_choose é a bebida escolhida pelo usuário'''

    if user_founds < MENU[drink_choose]['cost']:
        print('Sorry that\'s not enough money. Money refunded.')
    elif user_founds == MENU[drink_choose]['cost']:
        decrease_ingredients(drink_choose)
        resources['money'] += user_founds
        print(f'Here is your {drink_choose}☕. Enjoy')
    elif user_founds > MENU[drink_choose]['cost']:
        decrease_ingredients(drink_choose)
        resources['money'] += user_founds
        change = user_founds - MENU[drink_choose]['cost'] 
        resources['money'] -= change
        print(f'Here is ${change:.2f} in change.')
        print(f'Here is your {drink_choose}☕. Enjoy')


machine_is_on = True
while machine_is_on:
    user_order = input('What would you like? (espresso/latte/cappuccino): ')

    if user_order == 'report':
        for item in resources:
            if item == 'water':
                print(f'{item.title()}: {resources[item]}ml')
            elif item == 'milk':
                print(f'{item.title()}: {resources[item]}ml')
            elif item == 'coffee':
                print(f'{item.title()}: {resources[item]}g')
            else:
                print(f'{item.title()}: ${resources[item]:.2f}')
    elif user_order == 'espresso':
        check_resources('espresso')
    elif user_order == 'latte':
        check_resources('latte')
    elif user_order == 'cappuccino':
        check_resources('cappuccino')
    else:
        machine_is_on = False
