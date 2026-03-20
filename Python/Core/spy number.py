# A Spy number is a number where:
# Sum of digits = Product of digits

# 1124
# Sum = 1 + 1 + 2 + 4 = 8
# Product = 1 × 1 × 2 × 4 = 8

n=int(input())

sum=0
t=n
product=1

while t>0:
    r=t%10
    sum+=r
    product*=r
    t=t//10
if sum==product:
    print("spy number")
else:
    print("Not a spy number")