# define class
class Test:

    def __init__(self):
        # define property
        self.name = 'This is test class.'
        self.desc = 'This is test class to test the oop in python.'
        print('called')
        print(self.name)
        print(self.desc)
        
    # define method
    def display(self):
        print('Display function')
        print(self.name)
        print(self.desc)

# make object
t = Test()

# print( t.name )
t.display()

# t1 = Test()
# t1.display()
