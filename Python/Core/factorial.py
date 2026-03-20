# Write a program to find sum of Factorials upto N Numbers like 0! + 1! + 2! + 3! + 4! + 5! +....upto n!?


def is_fact(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    return fa
n=int(input())

sum=c=0

for i in range(0,n+1):
    sum+=is_fact(i)
    if i < n:
        print(is_fact(i), end="+")
    else:
        print(is_fact(i), end="")
    print("=", end="")
    print(sum)



