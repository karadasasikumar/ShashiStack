#  Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
# What happens if the lists are of unequal length?

a=[1, 2, 3, 4]
b=[10, 20, 30, 40]

#using  map() lambda function

s=list(map(lambda x,y: x+y,a,b))
print(s)

#@2question
#Given a list
# nums = [12, 15, 7, 18, 20, 21, 25]
# Use filter() and lambda to keep numbers that are divisible by 3 OR divisible by
# 5 but NOT divisible by both.
# Explain how the logical condition works

nums = [12, 15, 7, 18, 20, 21, 25]

s=list(filter(lambda x:(x%3==0 and x%5!=0) or (x%5==0 and x%3!=0),nums))
print(s)

from functools import reduce
# @3rd question
#  Given a list:
# nums = [1, 2, 3, 4]
# Use reduce() with a lambda to compute the sum, but start with an initial value
# of 10.
# Explain how the initial value affects the reduction process.


nums = [1, 2, 3, 4]

s=reduce(lambda x,y:x+y,nums,10)
print(s)

