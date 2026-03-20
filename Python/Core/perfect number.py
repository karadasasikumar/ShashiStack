# A Perfect number is a number where the sum of its factors (excluding itself) is equal to the number.

# 6 → factors: 1, 2, 3
#  # 1 + 2 + 3 = 6


n=int(input())
sum=0

for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Perfect number")
else:
    print("Not a perfect number")