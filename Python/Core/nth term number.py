# write a program to print "Nth" prime number

def is_prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False

n=int(input())

c=0
num=2

while True:
    if is_prime(num):
        c+=1
    if c==n:
        print(f"Nth prime number is ,{num}")
        break
    num+=1

