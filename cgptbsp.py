class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"my name ist {self.name}.")
    def show_age(self):
        print(f"I am {self.age} years old.")

class Student(Person):
    def study(self):
        print(f"{self.name} is a student")
        super().show_age()

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is a teacher")
        super().show_age()

def main():
    #student1 = Student("Felix", 19)
    #student1.introduce()
    #student1.study()

    Vehicle1 = Car("Car", 180)
    Vehicle2 = Bicycle("Bicycle", 20)

    Vehicle2.ride()
    Vehicle1.drive()




class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def describe(self):
        print(f"This Vehicle is a {self.brand}")
    def show_speed(self):
        print(f"Maximum speed is {self.max_speed}")
class Car(Vehicle):
    def drive(self):
        print(f"This Vehicle is a car!")
        super().show_speed()
class Bicycle(Vehicle):
    def ride(self):
        print(f"This Vehicle is a Bicycle!")
        super().show_speed()


if __name__ == "__main__":
    main()