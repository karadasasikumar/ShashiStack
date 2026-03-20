# Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.	Creating multiple loan accounts.
# 2.	Updating interest rates.
# 3.	Checking eligibility and total repayment for borrowers


class Loan:
    interest_rate=0.1
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def total(self):
        return self.principal + self.principal *Loan.interest_rate/100
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate
    @staticmethod
    def eligibility(salary):
        if salary>20000:
            return "Eligible for Loan"
        else:
            return "Not Eligible"

l1=Loan("shashi",10000)
l2=Loan("lucky",300000)

print(l1.name,l1.total())
print(l2.name,l2.total())

print(Loan.eligibility(30000))

Loan.change_interest_rate(0.2)

print(l1.total())
print(l2.total())

