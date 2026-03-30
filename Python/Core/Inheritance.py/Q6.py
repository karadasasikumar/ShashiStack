 # Create class University with a class variable and a class method. Inherit it
# into class College and access the parent’s class variable from the child class.

class University:
    name="JNTU-GV"
    @classmethod
    def show(cls):
        print(cls.name)

class College(University):
    def show(self):
        print(self.name)

c=College()
c.show()
c.show()