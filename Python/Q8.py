# . Create a class Member that:
# •	Has a shared BMI limit for “fit” status.
# •	Each member stores name, height, weight.
# •	Has a method to calculate BMI and check fit status.
# •	Provides a function to update BMI limit for all members.
# •	Offers a tool to check  if height and weight entered are valid numbers.
# Demonstrate:
# 1.	Creating multiple members.
# 2.	Updating BMI standard.
# 3.	Displaying fit status and input validity.

class Member:
    BMI_limit=25
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def calculate(self):
        self.calculate=self.height/self.weight
        if self.calculate>=self.BMI_limit:
            print("unfit")
        else:
            print("fit")
    @classmethod
    def update(cls,new):
        cls.BMI_limit=new
    @staticmethod
    def valid(height,weight):
        return height>0 and weight>0

m1=Member("shashi",5.5,53)

m1.calculate()

print(m1.valid(5.5,53))

Member.update(27)

m1.calculate()
