numberOfStudents = int(input("enter the number of students"))
for numberOfStudents in range(0, numberOfStudents) :
  numberOfMarks = int(input("enter the number of marks"))
  print(f"enter for student  {numberOfStudents+1} ")
  my_marks = []
  for numberOfStudents in range(0, numberOfMarks):
       marks = int(input(f"Enter Mark  {numberOfStudents+1} :"))
       my_marks.append(marks)
  average = sum(my_marks)/numberOfMarks
  print("The Average= ", average)
  print("The max Marke  = ", max(my_marks))
  print("The main Marke  =", min(my_marks))


