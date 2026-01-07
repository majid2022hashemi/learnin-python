class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):                                      # Added method
        return f'[Person: {self.name} ${self.pay:,}]'        # String to print
    
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        super().giveRaise(percent + bonus)


if __name__ == '__main__':
 
    bob = Person('Bob', pay=100)

    tom = Manager('Tom', pay=100)

    bob.giveRaise(.10)
    tom.giveRaise(.10)

    print(bob)
    print(tom)