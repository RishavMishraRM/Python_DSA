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



S = [Student('aaa', 101, 90), Student('bbb', 102, 80), Student('ccc', 103, 70)]

for i in S:
    i.display()