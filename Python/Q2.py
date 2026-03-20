# Create an Employee class that:
# •	Keeps a minimum experience required for promotion (shared across all employees).
# •	Stores employee name, experience, and department.
# •	Has a method to check eligibility for promotion.
# •	Provides a function to update promotion criteria globally.
# •	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.	Creating employees from different departments.
# 2.	Changing promotion criteria.
# 3.	Displaying eligibility results and department validation.


class Employee:
    min_exp=5
    def __init__(self,name,exp,dept):
        self.name=name
        self.exp=exp
        self.dept=dept
    def check_promotion(self):
        if self.exp>0:
            return "Eligible"
        else:
            return"Not Eligible"
    @classmethod
    def change_min_exp(cls,new_exp):
        cls.min_exp=new_exp
    def valid_dept(self):
        return self.dept in ["HR","Tech","Admin"]

e1=Employee("Shashi",2,"HR")
e2=Employee("lucky",3,"Tech")

print(e1.name,e1.check_promotion(),e1.valid_dept())
print(e2.name,e2.check_promotion(),e2.valid_dept())

Employee.change_min_exp(3)

print(e1.name,e1.check_promotion(),e1.valid_dept())
print(e2.name,e2.check_promotion(),e2.valid_dept())