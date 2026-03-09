# # Question 1:
from functools import reduce
l=[1,2,6,5,2,3,8,9,12]

result=reduce(lambda x,y:x+y,filter(lambda x:x%7==0,map(lambda x:x**3,l)),0)
print(result)