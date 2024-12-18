class CoffeeMachine:
    def __init__(self):
        # Initialize the coffee machine resources and menu
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money = 0
        self.menu = {
            "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
            "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
        }

    def report(self):
        # Print the current resources and money in the machine
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money:.2f}")

    def is_resource_sufficient(self, drink):
        # Check if there are enough resources to make the selected drink
        for item, required in drink["ingredients"].items():
            if self.resources.get(item, 0) < required:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        # Process the user's coin input and calculate the total amount
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return round(total, 2)

    def check_transaction(self, payment, cost):
        # Check if the user has inserted enough money for the drink
        if payment < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif payment > cost:
            # Provide change if the user inserted more money than required
            change = round(payment - cost, 2)
            print(f"Here is ${change:.2f} in change.")
        return True

    def make_coffee(self, drink_name, drink):
        # Deduct the ingredients from the machine's resources and prepare the coffee
        for item, amount in drink["ingredients"].items():
            self.resources[item] -= amount
        self.money += drink["cost"]
        print(f"Here is your {drink_name}. Enjoy!")

    def start(self):
        # Main loop to run the coffee machine
        machine_on = True
        while machine_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                # Turn off the coffee machine
                machine_on = False
                print("Turning off the coffee machine.")
            elif choice == "report":
                # Print the current resources and money
                self.report()
            elif choice in self.menu:
                # Process the user's drink choice
                drink = self.menu[choice]
                if self.is_resource_sufficient(drink):
                    payment = self.process_coins()
                    if self.check_transaction(payment, drink["cost"]):
                        self.make_coffee(choice, drink)
            else:
                # Handle invalid input
                print("Invalid choice. Please select espresso, latte, or cappuccino.")

if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.start()
