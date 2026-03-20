 # Create an iterator that yields words from a sentence one by one.

class Iterator:
    def __init__(self,s):
        self.s=s.split()
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i>=len(self.s):
            raise StopIteration
        s=self.s[self.i]
        self.i+=1
        return s

obj1=Iterator("Shashii is a good boii")

for i in obj1:
    print(i)