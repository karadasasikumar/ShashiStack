# sum of alternative fibanocii numbers

s=int(input())
e=int(input())
a,b=0,1
c=0
sum=0
ac=0
while a<e:
    if a>=s:
        c+=1
        if c%2==1:
            ac+1
            sum+=a
        co=a+b
        a=b
        b=co
if ac==0:
    print("No fibonacii numbers")
else:
    avg=sum/c
    print(f"{avg:.2f}")

