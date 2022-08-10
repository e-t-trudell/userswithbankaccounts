class BankAccount:
    # create two accounts for the each user(checking / saving)
    # create transfer method for user that takes money from a different user's(2) account(checking) and transfers it into another users(1) account(saving)
    def __init__(self, amount, account_type):
        self.amount = amount
        self.balance = 0
        self.balance = self.balance + amount
        self.interest_rate = 0.01
        self.account_type = account_type
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        # print(self.balance)
        return self
    def withdraw(self, amount):
        self.amount = amount
        if(self.balance <= amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
            # print (self.balance)
        return self
    def display_account_info(self):
        print(f"Savings Balance: $ {self.balance}")
        return self
    def yield_interest(self):
        if(self.balance < 0):
            print("not interested")
        elif(self.balance > 0):
            # print(self.balance + (self.balance * self.interest_rate))
            return self
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(200)
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email) 
        print(self.age) 
        print(self.gold_card_points)
        print(self.is_rewards_member)
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        # print(self.gold_card_points)
        # print(self.is_rewards_member)
        if(self.is_rewards_member==True):
            # print("New Enrollment!")
            return False
        else: 
            return True
    def spend_points(self,amount):
        self.amount = amount
        self.gold_card_points = self.gold_card_points - amount
        # print(amount)
        # print(self.gold_card_points)
        if(self.gold_card_points<=amount):
            print("Not enough points")
        elif(self.gold_card_points>=amount):
            return self
    def make_deposit(self,amount):
        self.amount = amount
        self.account.deposit(100)
        # print(self.account.balance)
        return self
    def make_withdrawal(self, amount):
        self.amount = amount
        self.account.withdraw(20)
        # print(self.account.balance)
        return self
    def display_user_balance(self):
        print(self.account.balance)
        print(f"User: {self.first_name},", "Checking Balance: ", self.account.balance)
        return self
one = User('Eric', 'Trudell', 'ettrudell17@gmail.com', 30)
two = User('Pickle', 'Rick', 'impicklerick!@gmail.com', 50)
one.enroll()
one.make_deposit(100).display_user_balance()
two.enroll()
two.make_withdrawal(20).display_user_balance()

