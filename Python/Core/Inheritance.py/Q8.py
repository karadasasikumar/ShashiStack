#  Create two classes Father and Mother, both defining a method skills(). Create
# class Child(Father, Mother) and check which skills() runs using MRO



class Father:
    def skills(self):
        print("Father skills")
        super().skills()

class Mother:
    def skills(self):
        print("Mother skills")

class Child(Father, Mother):
    def skills(self):
        print("Child skills")
        super().skills()

c = Child()
c.skills()
