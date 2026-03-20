# Implement a generator that yields running maximum from a list Example:
# [3,1,4,2] → 3, 3, 4, 4

def max(list):
    m=list[0]
    for i in list:
        if i>m:
            m=1
            yield m

nums=[3,1,4,2]

for x in max(nums):
    print(x)



