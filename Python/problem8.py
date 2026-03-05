# Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18


class Course:
    total_students=0
    def __init__(self,name):
        self.name=name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>18


s1=Course("sashi")
s2=Course("lucky")

s1.enroll()
s2.enroll()

print(s2.total_students)
print(s1.is_eligible(20))
print(s2.is_eligible(15))
