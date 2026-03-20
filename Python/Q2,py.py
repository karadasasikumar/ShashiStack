# 2. Create an iterator that returns only even numbers from a given list.

class Eveniterator:
    def __init__(self,n):
        self.n=n
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        for i in range(self.count,len(self.n)):
            self.count=i+1
            if self.n[i]%2==0:
                return self.n[i]
        raise StopIteration

obj1=[1,2,3,4,5,6,22,16]

even_numbers=Eveniterator(obj1)

for i in even_numbers:
    print(i)