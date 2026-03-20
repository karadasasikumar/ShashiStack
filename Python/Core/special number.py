# A Special number is a number where:
#
# Sum of factorial of digits = the number itself


# 145
#  Digits: 1, 4, 5
#  Factorials:
#
# 1! = 1
# 4! = 24
# 5! = 120
# Sum = 1 + 24 + 120 = 145

n=int(input())

sum=0
t=n

while t>0:
    r=t%10

    fact=1
    for i in range(1,r+1):
        fact*=i
    sum+=fact
    t=t//10
if sum==n:
    print("special number")
else:
    print("Not a special number")
