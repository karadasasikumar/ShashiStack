# l=[[1,2], [3,4], [5,6]]
#
# k=list(map(lambda x: x+[5], l))
# print(k)

# d={"apple":100, "banana":40, "cherry":150}
# print(d.keys())
# print(d.values())
# print(d.items())
# f= dict(filter(lambda x:x[1]>50,d.items()))
# print(f)

#split()
# k=input()
# print(k.split("$"))
# print(type(k))

# from functiontools import tool

#10th Question

# l=[5,10,15,20,25,30]
# sq= list(map(lambda x: x**2,l))
# print(sq)
# di=list(filter(lambda x: x%5 == 0,sq))
# v=reduce(lambda x,y: x+y,di)
#
# v=reduce(lambda x,y: x+y, filter(lambda x: x% 5 == 0, map(lambda x:x+2,l)))
# pprint(v)