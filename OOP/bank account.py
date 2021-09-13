class BankAccount:
    def __init__(self):
        self.balance = 0

    def create_account(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def add_money(self, money):
        self.balance += money
        print(money, ' Deposit Accepted')
        print('New balance is:', self.balance)

    def get_money(self, money):
        if money > self.balance:
            return 'Funds Unavailable'
        else:
            self.balance -= money
            print(money, ' Withdrawal Accepted')
            print('remaining balance is:', self.balance)


class SavingAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)

    def get_money(self, money):
        if money > self.balance:
            return 'Funds Unavailable'
        else:
            self.balance -= money
            print(money, ' Withdrawal Accepted')
            print('remaining balance is:', self.balance)


ba = BankAccount()
ba.create_account('asad awan', 1850)

ba.get_money(250)

ba.add_money(600)

sa = SavingAccount()

sa.get_money(2500)
