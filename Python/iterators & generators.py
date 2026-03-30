#  Implement an iterator that iterates over a string character by character in
# reverse order

class Iterator:
    def __init__(self,string):
        self.string=string
        self.index=len(string)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<0:
            raise StopIteration
        x=self.string[self.index]
        self.index-=1
        return x

s="Shashi"

for x in Iterator(s):
    print(x)

# in generator

def Iterator(string):
    index=len(string)-1

    while index>=0:
        yield string[index]
        index-=1

s="Shashii"

for x in Iterator(s):
    print(x)