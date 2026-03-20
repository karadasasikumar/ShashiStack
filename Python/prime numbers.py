#print to avg prime numbers in Given range
# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             return True
#         else:
#             return False
#
# s=int(input())
# e=int(input())
# c=0
# sum=0
#
# if s<=0 and i<=0:
#     print("Invalid Range")
# else:
#     for i in range(s,e+1):
#         b=is_prime(i)
#         if b==True:
#             c+=1
#             if c%2==1:
#                 sum=sum+i
#     if sum!=0:
#         r=float(sum/c)
#         print(f'{r:.3f}')

#2nd question

#print sum of all prime numbers

def is_prime(n):
    fc=0
    for i in range(1,n+1):


