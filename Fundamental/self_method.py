class Student:
    def __init__(myself, name, roll, marks):
        myself.name = name
        myself.roll = roll
        myself.marks = marks
        

    def display(self):
        print('Student Name:', self.name)
        print('Roll Number:', self.roll)
        print('Marks:', self.marks)


S = [Student('aaa', 101, 90), Student('bbb', 102, 80), Student('ccc', 103, 70)]
S.display() # Error: 'list' object has no attribute 'display'

