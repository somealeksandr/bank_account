# Написати клас "Банківський рахунок" (Account), який містить: 

# Номер рахунку 
# Розмір коштів на рахунку 
# Назва валюти рахунку (рублі, гривні, евро тощо), для позначення якої можна скористатись одним символом: R, G, E, $ тощо 
# Забезпечити можливість: 
# Відкривати рахунок та первинно вносити гроші на рахунок 
# Знімати гроші з рахунку 
# Докладати гроші на рахунок 




from random import randint
class Account:
    def __init__(self, card_number, amount, currency):
        self.__card_number = card_number
        self.__amount = amount
        self.__currency = currency
        print("Account constructor")

    def get_amount(self):
        return self.__amount

    def set_amount(self, new_amount):
        if self.__amount == new_amount:
            print("The same amount")
        else:
            self.__amount = new_amount       
    def drop(self, add_money):
        self.__amount = self.__amount + add_money

    def take_off(self, take_off_money):
        if self.__amount >= take_off_money:
            self.__amount = self.__amount - take_off_money
        else:
            print("Не достатьно коштів на рахунку")       
    
    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount: ", self.__amount, "\nCurrency: ", self.__currency)
        
while True:
    print("""
          ----------- MENU -------------------
          press 1 to create new Account
          press 2 to enter drop money to your Account
          press 3 to take of from your Account
          press 4 to show info
          press 0 to exit..
          """)
    try:
        choice = int(input())
        if choice == 1:
            amount = int(input("Enter amount money\n"))        
            currency = input("Enter currency: UAH  USD  EUR\n")
            card_number = randint(1000000, 9999999)
            credit_card = Account(card_number, amount, currency)
        elif choice == 2:
            new_balance = int(input("Enter when drop money: \n"))
            credit_card.drop(new_balance)
        elif choice == 3:
            new_balance = int(input("Enter when take off money: \n"))
            credit_card.take_off(new_balance)
        elif choice == 4:
            credit_card.show_info()        
        elif choice == 0:
            try:
                print("Bye!")
                break
            except Exception as err:
                print(err)

    except Exception as err:
        print("Somthing Error", err)              
    
    