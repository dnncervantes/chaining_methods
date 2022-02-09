class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self, amount):
        self.amount -= amount
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    # def transfer_money(self,amount,user):
    #     self.amount -= amount
    #     user.amount += amount
    #     self.display_user_balance()
    #     user.display_user_balance()

danny = User("Danny")
sara = User("Sara")
matt = User("Matt")

danny.make_deposit(1000).make_withdrawl(500).display_user_balance()

sara.make_deposit(5000).make_deposit(100).make_withdrawl(600).display_user_balance()

matt.make_deposit(10000).make_deposit(200).make_withdrawl(5200).display_user_balance()