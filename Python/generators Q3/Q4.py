 # Implement a generator that yields vowels from a string.


def vowels(s):

    """Generator that yields vowels from a given string s."""
    vowels="aeiouAEIOU"

    for i in s:
        if i in vowels:
            yield i

for i in vowels("Shashi"):
    print(i)


