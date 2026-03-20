# Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.	Creating multiple products.
# 2.	Changing the tax rate.
# 3.	Showing updated prices and validity checks.ca



class Product:
    tax_rate=0.1
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def final_price(self):
        tax=self.price*Product.tax_rate
        return self.price+tax
    @classmethod
    def change_tax_rate(cls,new_tax):
        cls.tax_rate=new_tax
    #function to check price validity or else we use to static method also
    def check_price(self):
        if self.price>0:
            return "Valid Price"
        else:
            return "Invalid Price"

p1=Product("laptop",500)
p2=Product("phone",100)

print(p1.name,p1.final_price(),p1.check_price())
print(p2.name,p1.final_price(),p1.check_price())

Product.change_tax_rate(0.2)


print(p1.name,p1.final_price())
print(p2.name,p2.final_price())