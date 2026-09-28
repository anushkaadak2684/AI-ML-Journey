class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        if not name.strip():
            return "Name cannot be empty"
        self.__name = name

    def set_roll_no(self, roll_no):
        if roll_no < 1 or roll_no > 100:
            return "Roll no. must be between 1 and 100"
        self.__roll_no = roll_no

    def set_marks(self, marks):
        if marks < 0:
            return "Marks cannot be negative"
        self.__marks = marks


s1 = Student("Anushka", 16, 98)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())

s1.set_marks(99)
print(s1.get_marks())

print(s1.set_roll_no(-3))
print(s1.get_roll_no())