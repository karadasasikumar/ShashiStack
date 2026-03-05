# Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount>0


class  BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        else:
            return False

ac1=BankAccount("sashi",1000)
print(ac1.holder,ac1.balance)
ac1.deposit(500)
print(ac1.balance)
BankAccount.change_bank_name("Union")
print(BankAccount.bank_name)
print(ac1.validate_amount(1000))