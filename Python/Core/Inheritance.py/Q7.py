#  Create class MathOps with a static method add(a, b). Create class
# AdvancedOps(MathOps) and use the static method without overriding it.

class MathOps:
    @staticmethod
    def add(a,b):
        return a+b
class AdvancedOps(MathOps):
    pass
print(AdvancedOps.add(2,3))
