import os

print("Current Working Directory:", os.getcwd())
import sqlite3
conn=sqlite3.connect("student.db")
cursor=conn.cursor()
command= "CREATE TABLE IF NOT EXISTS student (name TEXT not null ,roll_no INTEGER PRIMARY KEY,marks INTEGER not null)"
conn.execute(command)
# print("Table Created")

def store(name,roll_no,marks):
    command=" insert into student (name,roll_no, marks ) values(?,?,?)"
    try:
        cursor.execute(command,(name,roll_no,marks))    
        conn.commit()
        print()
    except sqlite3.IntegrityError:
        print("Student already exists")
    # command="select * from student where roll_no = ?"
    # result=cursor.execute(command,(roll_no,))
    # r=result.fetchone()
    # if r:
    #     print(" Student already there !!")
    # else:    
    #     command=" insert into student (name,roll_no, marks ) values(?,?,?)"
    #     cursor.execute(command,(name,roll_no,marks))
    #     conn.commit()
    #     print("Student Data stored ")



def delete(roll_no):
    command="delete from student where roll_no = ?"
    cursor.execute(command,(roll_no,))
    if cursor.rowcount == 0:
       print("Student not in database !! ")
    else:
        conn.commit()
        print("Student deleted !! ")
        print()
        
    # command="select * from student where roll_no = ?" 
    # result=cursor.execute(command,(a,))
    # r=result.fetchall()
    # if r:
    #     command="delete from student where roll_no = ?"
    #     cursor.execute(command,(a,))
    #     conn.commit()
    #     print("Student deleted !! ")
    # else:
    #     print("Student not in database !! ")


def update(roll_no,marks):
    command="update student set marks = ? where roll_no = ?"
    cursor.execute(command,(marks,roll_no))
    if cursor.rowcount==0:
        print("Student not in Database !!")
    else:
        conn.commit()
        print("Student marks updated !!")
    # command="select * from student where roll_no= ?"
    # result=cursor.execute(command,(roll_no,))
    # r=result.fetchone()
    # if r:
    #     command="update student set marks = ? where roll_no = ?"
    #     cursor.execute(command,(marks,roll_no))
    #     conn.commit()
    #     print("Student marks updated !!")
    # else:
    #     print("Student not in database !!")


def search(roll_no):    
    command="select * from student where roll_no = ? "
    cursor.execute(command,(roll_no,))
    return cursor.fetchone()
    # result=cursor.execute(command,(roll_no,))
    # r=result.fetchone()
    # if r:
    #     print(r)
    # else:
    #     print("Student not in Database !!")


def display_all():
    command="select * from student "
    result=cursor.execute(command)
    r=result.fetchall()
    if r:
        for name, roll_no, marks in r:
            print(f"Name: {name}")
            print(f"Roll No: {roll_no}")
            print(f"Marks: {marks}")
            print() 
    else:
        print("NO Student in the Database")