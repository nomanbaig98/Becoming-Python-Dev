class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, add):
        self.balance += add
        print('cash deposited:', add)
        print('new balance is: ', self.balance)

    def withdraw(self, sub):
        if sub > self.balance:
            print('funds unavailable')
        else:
            self.balance -= sub
            print('cash withdrawn:', sub)
            print('remaining balance is: ',self.balance)

    def __str__(self):
        return f'Account Owner: {self.owner} \nAccount balance:  {self.balance}'

acc1 = BankAccount('noman',5000)
print(acc1)
print(acc1.owner)
print(acc1.balance)
acc1.deposit(500)
# print(acc1.balance)
acc1.withdraw(550)
acc1.withdraw(5000)