import mysql.connector
n=input("ENTER YOUR MYSQL PASSWORD:")
con=mysql.connector.connect(host="localhost",user="root",passwd="79sumathi",database="employee")
c=con.cursor()
c.execute("CREATE TABLE student_attendance (Roll_No int(6) Primary Key,Present int(5),Total int(5))")
c.execute("CREATE TABLE student_fees(Roll_No int(6)  Primary Key,Fees_Paid int(10) ,Fees_rem int(6))")
c.execute("CREATE TABLE student_data(Roll_No int(6)  Primary Key,Name char(30),email char(30),Gender char(7),Phone int(10),DOB date,Location char(30))")
c.execute("CREATE TABLE student_marks (Roll_no int(6) primary key,Physics int(3),Chemistry int(3), Mathematics int(3), English int(3), Comp_Science int(3), Biology int(3))")
print("No Errors")


