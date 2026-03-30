# Create multi-level inheritance with classes A → B → C, each having a method
# display() printing the class name. Create object of C and call display(),
# showing method resolution.


class A:
    def __init__(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("This is class B")
        super().__init__()

class C(B):
    def __init__(self):
        print("This is class C")
        super().__init__()

obj=C()

