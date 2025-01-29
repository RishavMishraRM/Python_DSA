class Student:
    college = 'IIT'
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        Student.college = 'IIT'
        
    def display(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)
        college = 'IIT' # it would work
        print('College:', Student.college)
        ## college = 'IIT' # Error: 'list' object has no attribute 'display', attribute error
        print()


Student.college = 'IIT' # it would work but if nothing is avialable above in class
S1 = Student('aaa', 101, 90)
S2 = Student('bbb', 102, 80)
S1.display() # Error: 'list' object has no attribute 'display'
S2.display() # Error: 'list' object has no attribute 'display'
