"""
Program: Creates a student class and associated unittest
Author: Ashley Fry
Last date modified: 04/22/2023
The purpose of this program is to create two student objects of class student. Associated unittest to test class student.
The input is student objects in main and 7 unittests testng student class
The output is display of student objects from student class and results from unittest
"""

class student:
    def __init__(self, lname, fname, major, gpa=0.0):

        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError

        if gpa and not 0 < gpa < 4:
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def set_last_name(self, lname):
         self.last_name = lname

    def set_first_name(self, fname):
         self.first_name = fname

    def set_address(self, major):
         self.major = major

    def set_phone_number(self, gpa):
         self.gpa = gpa

    def display(self):
        return str(self.first_name) + " " + str(self.last_name) + "\n" + str(self.major) + "\n" + str(self.gpa) + "\n"

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

    def __repr__(self):
        return "StudentClass(\"" + self.first_name + "\", \"" + self.major + "\", \"" + str(self.gpa) + "\")"

if __name__ == "__main__":
    test_student_1 = student('Duck', 'Donald', 'Computer Engineering', 2.75)
    test_student_2 = student('Mouse', 'Minnie', 'Network Architect', 3.8)

    print(test_student_1.display())
    print(test_student_2.display())