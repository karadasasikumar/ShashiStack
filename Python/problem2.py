# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.


class Employee:
    company_name="TestCorp"
    def __init__(self,name):
        self.name=name

    @classmethod
    def change_company(cls, new_name):
        cls.company_name=new_name

e1=Employee("Sashi")
e2=Employee("sasi")

Employee.change_company("Infotech")

print(e1.name,e1.company_name)
print(e2.name,e2.company_name)