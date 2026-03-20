# Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.	Creating multiple courses.
# 2.	Enrolling students.
# 3.	Updating minimum duration and checking durations.


class Course:
    total_course=0
    min_duration=1
    def  __init__(self,title,duration,students):
        self.title=title
        self.duration=duration
        self.students=students
        Course.total_course+=1
    def add_student(self):
        self.students+=1
    @classmethod
    def change_min_duration(cls,new_duration):
        cls.min_duration=new_duration
    @staticmethod
    def check_duration(duration):
        if duration >0:
            return "Valid"
        else:
            return "Not Valid"

c1=Course("Python",30,20)

print(Course.total_course)
c1.add_student()

print(c1.title,c1.duration,c1.students)

Course.change_min_duration(30)

print(Course.check_duration(30))


