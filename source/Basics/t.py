# Python program to explain property() function

# Alphabet class
class Alphabet:
    def __init__(self, x):
        self.v = x

    # getting the values
    def getValue(self):
        print('Getting value')
        return self.v

    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self.v = value

    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self.v

    t = property(getValue, setValue, delValue, )


# passing the value
x = Alphabet('GeeksforGeeks')
print(x.t)

x.t = 'GfG'

del x.t
