#encapulactions
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.__marks = marks #private variable

    #Method update marks
    def update_marks(self, new_marks):
        self.__marks = new_marks

#Method to get marks
    def get_marks(self):
        return self.__marks #__marks is private variable
    
    def is_pass(self):
        return self.marks >= 40
    
#Testing the Student class
student1 = Student("Alice", 20, 85)
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
print(student1.get_marks())  # Output: 85
student1.update_marks(90)
print(student1.get_marks())  # Output: 90
print(student1.is_pass())  # Output: True