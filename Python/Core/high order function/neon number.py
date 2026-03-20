# A Neon number is a number where the sum of digits of its square = the number itself.
# ex:9
# Square = 9 × 9 = 81
# Digits sum = 8 + 1 = 9


n=int(input())

sum=0
sq=n*n

while sq>0:
    sum+=sq%10
    sq=sq//10
if sum==n:
    print("Neon Number")
else:
    print("Not a neon number")