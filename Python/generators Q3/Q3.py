 # Write a generator that yields digits from an integer one by one.

# in String method

# def digit_string(n):
#
#     """generator that yields digits from an integer using string conversion"""
#     for i in str(n):
#         yield int(i)
#
#
#
# for i in digit_string(12345):
#     print(i)


#mathmatic model

def digit_math(n):


    """generator that yields digits from an integer using string conversion"""

    div=1
    while n//div>=0:
        div*=10

    while div>0:
        digit=n//div
        yield digit
        n%=div
        div//=10

for digit in digit_math(12345):
    print(digit)


