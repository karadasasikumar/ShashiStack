# A Pronic number is a number that is the product of two consecutive numbers.

# 2×3 = 6
# consecutive numbers

n=int(input())

for i in range(1,n+1):
    if i*(i+1)==n:
        print("Pronic Number")
        break
else:
    print("not a pronic number")