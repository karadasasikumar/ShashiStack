# Create an iterator that yields words from a sentence one by one.

class Iterator:
    def __init__(self,sentence):
        self.sentence=sentence.split()
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.sentence):
            raise StopIteration
        sentence=self.sentence[self.index]
        self.index +=1
        return sentence

s="i love shashi"
for x in Iterator(s):
    print(x)