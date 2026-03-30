# Create class Employee with an instance method salary(). Create class
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
# both outputs

class Employee:
    def salary(self):
        print("Salary=2000")
class Manager(Employee):
    def salary(self):
        super().salary()
        print("Incentive=5000")

m=Manager()
m.salary()