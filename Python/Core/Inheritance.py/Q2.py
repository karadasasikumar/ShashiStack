#  Create class A with method show(). Create class B(A) that overrides show() and
# also calls the parent method using super()

class A:
    def show(self):
        print("This is class A")
class B(A):
    def show(self):
        super().show()
        print("This is class B")

obj=B(026)
obj.show()