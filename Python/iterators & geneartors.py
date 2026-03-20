# Write a custom iterator that prints numbers from 1 to N

class Iterator:
    def __init__(self,n):
        self.n=n
        self.count=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>self.n:
            raise StopIteration
        result=self.count
        self.count+=1
        return result

obj1=Iterator(5)
for i in obj1:
    print(i)

