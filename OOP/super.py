class User:
    def __init__(self, email):
        self.email = email

    def signed_in(self):
        print('User logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)  # same as using the below command, it doesn't take self parameter
        # User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} is attacking with {self.power} power')


wizard1 = Wizard('joe', 89, 'joe@live.com')

wizard1.attack()
print(wizard1.email)
