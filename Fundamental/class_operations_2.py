class Student:
    '''This is version 1.0'''

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def __str__(self):
        return 'This is Student Class'
    
    def display(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)



S1 = Student('aaa', 101, 90)
S2 = Student('bbb', 102, 80)
S3 = Student('ccc', 103, 70)
S1.display()
S2.display()
S3.display()