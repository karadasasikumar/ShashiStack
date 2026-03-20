# A Harshad number (also called Niven number) is a number that is divisible by the sum of its digits.

# 18
# Digits: 1 + 8 = 9
# 18 ÷ 9 = 2 ✅ → Harshad

n=int(input())

t=n
sum=0

while t>0:
    sum+=t%10
    t=t//10
if n%sum==0:
    print("Harshad Number")
else:
    print("not a harshad number")