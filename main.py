
from student import Student
from student import StudentManagementSystem



# menu code
sms=StudentManagementSystem()
while(True):
    print("---MENU---")
    print("\n 1.Enter new student ")
    print("\n 2.Search a student ")
    print("\n 3.Display all students and detail ")
    print("\n 4.Delete student detail ")
    print("\n 5.Update mark of the student ")
    print("\n 6.Exit")
    try:
        ch=int(input("Enter your choice : "))
    except ValueError:
        print("Integer Only !!")
    else:
        match ch:
            case 1:
                name=input("Enter student name : ")
                roll_no=int(input("\nEnter the Roll.No of the student : "))
                marks=int(input("\nEnter the marks of the student : "))
                stu1=Student(name,roll_no,marks)
                sms.add_student(stu1)
            case 2:
                r=int(input("Enter the Roll.no of student to be search : "))
                sms.search_student(r)
            case 3:
                sms.display_all_students()
            case 4:
                r=int(input("Enter the Roll.no of student to be deleted : "))
                sms.delete_student(r)
            case 5 :
                r=int(input("Enter the Roll.no of student to be updated : "))
                m=int(input("Enter the new marks of the student :"))
                sms.update_student_marks(r,m)
            case 6:
                break
            case _:
                print("Invalid Choice ")

