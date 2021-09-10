class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, add):
        self.balance += add
        print('cash deposited:', add)
        return 'new balance is: ' + str(self.balance)

    def withdraw(self, sub):
        if sub > self.balance:
            return 'funds unavailable'
        else:
            self.balance -= sub
            print('cash withdrawn:', sub)
            return 'remaining balance is: '+ str(self.balance)

    def __str__(self):
        return f'Account Owner: {self.owner} \nAccount balance:  {self.balance}'

acc1 = BankAccount('noman',5000)
print(acc1)
print(acc1.owner)
print(acc1.balance)
print(acc1.deposit(500))
# print(acc1.balance)
print(acc1.withdraw(550))
print(acc1.withdraw(5000))