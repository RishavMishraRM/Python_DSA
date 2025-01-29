class Student:
    def __init__(self):
        self.name = 'abc'
        self.roll = 101
        self.marks = 78.25
        print('In Constructor')

    def display(self):
        print(self.name, self.roll, self.marks)



S = Student()
S.__init__() # Init Constructor will be called again and an object will be created again
