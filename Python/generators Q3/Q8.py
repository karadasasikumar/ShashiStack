 # Create an iterator that returns only even numbers from a given list.

class Even_num:
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        x=self.data[self.index]
        self.index+=1

        if x%2==0:
            return x
        else:
            return self.__next__()

nums=[1,2,3,4,5,6]

for i in Even_num(nums):
    print(i)


# in generator

def Even(n):
    for num in n:
        if num%2==0:
            yield num


s=[1,2,3,4,5,6]

for i in Even(s):
    print(i)




