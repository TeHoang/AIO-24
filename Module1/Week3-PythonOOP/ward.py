class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        print(f" - Name: {self.name} - YoB: {self.yob} - ", end="")


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print("Student", end="")
        super().describe()
        print(f"Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print("Teacher", end="")
        super().describe()
        print(f"Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print("Doctor", end="")
        super().describe()
        print(f"Specialist: {self.specialist}")


class Ward():
    def __init__(self, name):
        self.store = []
        self.name = name

    def add_person(self, person):
        self.store.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.store:
            person.describe()

    def count_doctor(self):
        return sum([isinstance(person, Doctor) for person in self.store])

    def sort_age(self):
        self.store.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers_yob = [
            person.yob for person in self.store if isinstance(person, Teacher)]
        return sum(teachers_yob) / len(teachers_yob)


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

# Student - Name: studentA  - YoB: 2010 - Grade: 7

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

# Teacher - Name: teacherA  - YoB: 1969 - Subject: Math

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists ")
doctor1.describe()

# Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists

print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

"""
Ward Name: Ward1
Student - Name: studentA - YoB: 2010 - Grade: 7
Teacher - Name: teacherA - YoB: 1969 - Subject: Math
Teacher - Name: teacherB - YoB: 1995 - Subject: History
Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists
Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists
"""

# 2(c)

print(f"\nNumber of doctors: {ward1.count_doctor()}")

# Number of doctors: 2

# 2(d)

ward1.sort_age()
ward1.describe()

"""
Number of doctors: 2
Ward Name: Ward1
Student - Name: studentA - YoB: 2010 - Grade: 7
Teacher - Name: teacherB - YoB: 1995 - Subject: History
Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists
Teacher - Name: teacherA - YoB: 1969 - Subject: Math
Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists
"""

# 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")

# Average year of birth (teachers): 1982.0
