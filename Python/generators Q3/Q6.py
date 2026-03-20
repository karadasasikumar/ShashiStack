 # Write an iterator that returns characters at even indices of a string.

class Iterator:
    def __init__(self,string):
        self.string=string
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i>=len(self.string):
            raise StopIteration
        x=self.string[self.i]
        self.i+=2
        return x

obj1=Iterator("SHASHII")

for i in obj1:
    print(i)
