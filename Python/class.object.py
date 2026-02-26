class Person:
    total_no_of_person=0

    def __init__ (self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        if phone:
           Person.total_no_of_person+=1
c1=Person("Sasi",21,1)
c2=Person("shashi",23,2)
print(Person.total_no_of_person)