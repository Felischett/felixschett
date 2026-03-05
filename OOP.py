class Parent:
    speaks = ["English"]

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")


class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def introduce(self):
       print(f"my name is {self.name}.")
   def show_age(self):
       print(f"I am {self.age} years old.")

class Student(Person):
   def study(self):
       print(f"{self.name} is a student.")
       super().show_age()

class Teacher(Person):
   def teach(self):
       print(f"{self.name} is a teacher")
       super().show_age()

student1 = Student("Felix", 19)
teacher1 = Teacher("Jonas", 15)


student1.introduce()
student1.study()
print()
teacher1.introduce()
teacher1.teach()