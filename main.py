class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money
        self.state = "choosing action"
        print("Write action (buy, fill, take, remaining, exit):")

    def get_status(self):
        print("\nThe coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')

    def change_amounts(self, water = 0, milk = 0, beans = 0, money = 0, cups = 0):
        self.water += water
        self.milk += milk
        self.coffee_beans += beans
        self.money += money
        self.cups += cups

    def check_resources(self, water, milk, beans, cups):
        if self.water - water < 0:
            print('Sorry not enough water')
        elif self.milk - milk < 0:
            print('Sorry not enough milk')
        elif self.coffee_beans - beans < 0:
            print('Sorry not enough beans')
        elif self.cups - cups < 0:
            print('Sorry not enough cups')
        else:
            return True

    def fill(self, amount):
        try:
            amount = int(amount)
        except:
            pass
        types = self.state.split()
        types.append('')
        if types[1] == 'water':
            self.change_amounts(water = amount)
            print("Write how many ml of milk do you want to add:")
            self.state = 'filling milk'
        elif types[1] == 'milk':
            self.change_amounts(milk = amount)
            print("Write how many grams of coffee beans do you want to add:")
            self.state = 'filling beans'
        elif types[1] == 'beans':
            self.change_amounts(beans = amount)
            print("Write how many disposable cups of coffee do you want to add:")
            self.state = 'filling cups'
        elif types[1] == 'cups':
            self.change_amounts(cups = amount)
            self.state = 'choosing action'
            print("\nWrite Action (buy, fill, take, remaining, exit):")
        else:
            print("\nWrite how many ml of water do you want to add:")
            self.state = 'filling water'

    def take_money(self):
        print("\nI gave you $" +str(self.money))
        self.money = 0

    def make_coffee(self, coffee_type):
        if coffee_type == 'back':
            pass
        elif coffee_type == '1':
            pass_check = self.check_resources(250, 0, 16, 1)
            if pass_check == True:
                self.change_amounts(-250, 0, -16, 4, -1)
                print('I have enough resources, making you an espresso!')
        elif coffee_type == '2':
            pass_check = self.check_resources(350, 75, 20, 1)
            if pass_check == True:
                self.change_amounts(-350, -75, -20, 7, -1)
                print('I have enough resources, making you a latte!')

        elif coffee_type == '3':
            pass_check = self.check_resources(200, 100, 12, 1)
            if pass_check == True:
                self.change_amounts(-200, -100, -12, 6, -1)
                print('I have enough resources, making you a cappuccino!')

        else:
            print("that type of coffee does not exist")

    def processing(self, input_in):
        if self.state == 'choosing action':
            if input_in == 'buy':
                self.state = 'choosing_coffee'
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif input_in == 'fill':
                self.state = 'filling'
                self.fill(input_in)
            elif input_in == 'take':
                self.take_money()
                print("\nWrite Action (buy, fill, take, remaining, exit):")
            elif input_in == 'remaining':
                self.get_status()
                print("\nWrite Action (buy, fill, take, remaining, exit):")
            elif input_in == 'exit':
                quit()
            else:
                print("I cannot do that action.")
        elif self.state == 'choosing_coffee':
            self.make_coffee(input_in)
            self.state = 'choosing action'
            print("\nWrite Action (buy, fill, take, remaining, exit):")
        elif self.state.split()[0] == 'filling':
            self.fill(input_in)



coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    coffee_machine.processing(input('> '))
