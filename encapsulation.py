# we use encapsulation to hide the internal state of an object and only expose a public interface. 
# Python has no private/public keywords, it uses naming conventions:
# name     -> public: can be accessed from anywhere
# _name    -> protected: by convention, don't use it outside the class or its subclasses
# __name   -> private: Python renames it internally (name mangling) so it's hard to access from outside

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._bank_name = "MyBank"  # protected
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Ali", 1000)
acc.deposit(500)
print(acc.get_balance())   # 1500
print(acc.owner)           # Ali
print(acc.__balance)       # AttributeError cuz __balance is private