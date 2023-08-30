# todo 1
name = input("Name ")
delivery_date = input("Delivery Date ")
print("Name: ", name)
print("Delivery Date: ", delivery_date)
# todo 2
import random
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000,10000)
        self.course_name = course_name
        self.course_mark=  course_mark
# user input for course name
# course_name = input("Enter course name: ")
# todo 3
class Student:
   total_student_count = 0  # Static variable to track the total student count

   def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(1000,10000)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_student_count += 1
   def enroll_course(self,course_name,course_mark):
       course=Course(course_name,course_mark)
       self.courses_list.append(course)

   def get_student_details(self):
       return {
           "student_name": student_name,
           "student_age": student_age,
           "student_number": student_number,
       }
   def get_student_course(self):
       return self.courses_list

   def print_student_courses(self):
       for course in self.courses_list:
           print(f"course :{course.course_name},  mark :{course.course_mark}")

   def get_student_average(self):
            if not  self.courses_list:
                return 0

            total_marks = sum(course.course_mark for course in self.courses_list )
            return total_marks / len(self.courses_list)

# TODO 9
students =[]

while True:
    try:
        selection = int(input(
            "1. Add New Student\n"
            "2. Delete Student\n"
            "3. Display Student\n"
            "4. Get Student Average\n"
            "5. Add Course to Student with Mark\n"
            "6. Exit"))
    except ValueError :
        print("invalid value")
        continue


    if selection==1:
        student_name = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_number = input("Enter student number: ")
        student = Student(student_name,student_age,student_number)
        students.append(student)
        print("Student Added Successfully")
    elif selection == 2:
        student_number == input("enter student number :")
        for student in students:
            if student.student_number==student_number:
                students.remove(student)
                print("student delet successfully")
            elif student.student_number==student_number :
                print("the student not found try again")
    elif selection== 3:
        student_number=input("enter student number :")
        for student in students:
            if student.student_number==student_number:
                print(student.get_student_details())
                print(student.print_student_courses())
                break
        else:
                print("the student not found try again")
    elif selection == 4:
        student_number = input("enter student number :")
        for student in students:
            if student.student_number==student_number:
                avareg=student.get_student_average()
                print("Student avareg :",avareg)
                break
        else:
                print("the student not found ")
    elif selection==5:
        student_number = input("enter student number :")
        for student in students:
            if student.student_number == student_number:
                course_name = input("enter the name of course :   ")
                course_mark=float(input("Enter course mark:  "))
                student.enroll_course(course_name,course_mark)
                print("course added successfully")
                break
        else:
            print("the student not found ")


    elif selection == 6:
        exit()


    else:print("invalid selection ")






























