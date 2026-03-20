# Write a program to print the Sum of the Armstrong Numbers in the Given Range?
#
#
# Constraints:
# Input          :- First Line of Input Consists of One Integer Value.
#
#                   Second Line of Input Consists of One Integer Value.
#
# Output        :- Print the Sum of All Armstrong Numbers.
#
# Constraints  :- Either of the Given Input is Equal to Zero then Print "Invalid Inputs".
#
#                       If there are No Armstrong Numbers Between the Given Range then, print "No Armstrong Numbers in a Given Range.
#
#                       If Either of the Given Inputs is Negative then Convert into Positive and then Print the Sum of all Armstrong Numbers.



def is_arm(n):
    t=n
    sum=0
    dc=0
    while t>0:
        r=t%10
        dc+=1
        n=t//10
    t=n
    while t>0:
        r=t%10
        sum=sum+(r**dc)
        n=t//10

s=int(input())
e=int(input())
sum=0
c=0

if s<=0 and e<=0:
    print("Invalid Inputs")
else:
    s=abs(s)
    e=abs(e)
    if s>e:
        s,e=e,s
    for i in range(s,e+1):
        if is_arm(i):
            sum+=1
            c+=1
            if c==1:
                print("Armstrong Numbers in the Given Range is ", end="")
            if c!=1:
                print(" + ",end="")
            print(" = ",sum)
