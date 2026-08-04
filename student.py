import database as db
class Student():
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll.No : {self.roll_no}")
        print(f"Marks : {self.marks}")
    def update_marks(self,new_mark):
        self.marks=new_mark
        print("Marks is updated succesfully !")
    def __str__(self):
        return f"{self.name} ({self.roll_no})"
    def __eq__(self, value):
        return self.roll_no == value.roll_no
    

class StudentManagementSystem:


    def add_student(self,stu):
       
        db.store(stu.name,stu.roll_no,stu.marks)
        
    def display_all_students(self):
     
        db.display_all()
        
    def search_student(self,roll_no):
       
        result=db.search(roll_no)
        if result:
            student = Student(result[0], result[1], result[2])
            student.display()
        
        else:
             print("Student not in Database !!")

    def delete_student(self,roll_no):
    
            db.delete(roll_no)
               
        

    def update_student_marks(self, roll_no, new_marks):
     
                db.update(roll_no,new_marks)
             
   
                
        
                           


# sms=StudentManagementSystem()
# while(True):
#     print("---MENU---")
#     print("\n 1.Enter new student ")
#     print("\n 2.Search a student ")
#     print("\n 3.Display all students and detail ")
#     print("\n 4.Delete student detail ")
#     print("\n 5.Update mark of the student ")
#     print("\n 6.Exit")
#     try:
#         ch=int(input("Enter your choice : "))
#     except ValueError:
#         print("Integer Only !!")
#     else:
#         match ch:
#             case 1:
#                 name=input("Enter student name : ")
#                 roll_no=int(input("\nEnter the Roll.No of the student : "))
#                 marks=int(input("\nEnter the marks of the student : "))
#                 stu1=Student(name,roll_no,marks)
#                 sms.add_student(stu1)
#             case 2:
#                 r=int(input("Enter the Roll.no of student to be search : "))
#                 sms.search_student(r)
#             case 3:
#                 sms.display_all_students()
#             case 4:
#                 r=int(input("Enter the Roll.no of student to be search : "))
#                 sms.delete_student(r)
#             case 5 :
#                 r=int(input("Enter the Roll.no of student to be search : "))
#                 m=int(input("Enter the new marks of the student :"))
#                 sms.update_student_marks(r,m)
#             case 6:
#                 break
#             case _:
#                 print("Invalid Choice ")

