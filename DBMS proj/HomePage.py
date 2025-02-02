'''from tkinter import *
from tkinter import ttk

import Login_Student
import Login_Employee

class Main_Page:
    def __init__(self, root, ls):
        self.root = root
        self.ls = ls
        # Creating the first frame.
        self.frame = Frame(root, bg='#add8e6')  # Light blue background color
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0]//9*2, y=ls[1]//4, width=ls[0]//9*5, height=ls[1]//4*2)

        # Taking All pics in the variable.
        self.photo_student = PhotoImage(file=r"Images/customer.png")
        self.photo_employee = PhotoImage(file=r"Images/admin.png")

        # Resizing the Images as per requirement.
        self.photo_student = self.photo_student.subsample(4, 4)
        self.photo_employee = self.photo_employee.subsample(4, 4)

        # Labeling the page.
        self.title = Label(self.frame, text='TVS MOTORS', font=('Algerian', 25, 'bold'), bg='red', fg='white')  # Red background color
        self.title.pack(side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='TVS HOMEPAGE', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(side=TOP)

        # Creating two buttons.
        self.student_btn = Button(self.frame1, text='CUSTOMER PORTAL', bd=0, bg='#ffffff', image=self.photo_student,
                                   compound=TOP, command=self.student) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9)*3-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)


        self.employee_btn = Button(self.frame1, text="ADMIN PORTAL", bd=0, bg='#ffffff', image=self.photo_employee,
                                   compound=TOP, command=self.employee) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9 * 5)-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)

    def student(self):
        self.frame.place_forget()
        student_menu = Login_Student.Student_Show(self.root, self.ls, self.frame)

    def employee(self):
        self.frame.place_forget()
        employee_menu = Login_Employee.Employee_Show(self.root, self.ls, self.frame)
'''
'''
from tkinter import *
from tkinter import ttk

import Login_Student
import Login_Employee

class Main_Page:
    def __init__(self, root, ls):
        self.root = root
        self.ls = ls

        # Load background image
        self.bg_image = PhotoImage(file=r"Images/tvs.png")

        # Creating the first frame with a label as the background image.
        self.frame = Label(root, bg='#add8e6', image=self.bg_image)
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Creating the first frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.5)

        # Taking All pics in the variable.
        self.photo_student = PhotoImage(file=r"Images/customer.png")
        self.photo_employee = PhotoImage(file=r"Images/admin.png")

        # Resizing the Images as per requirement.
        self.photo_student = self.photo_student.subsample(4, 4)
        self.photo_employee = self.photo_employee.subsample(4, 4)

        # Labeling the page.
        self.title = Label(self.frame, text='TVS MOTORS', font=('Algerian', 25, 'bold'), bg='red', fg='white')  # Red background color
        self.title.pack(side=TOP)

        # Title for Register/Login.
        self.title1 = Label(self.frame1, text='TVS HOMEPAGE', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(side=TOP)

        # Creating two buttons.
        self.student_btn = Button(self.frame1, text='CUSTOMER PORTAL', bd=0, bg='#ffffff', image=self.photo_student,
                                   compound=TOP, command=self.student)
        self.student_btn.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.4)


        self.employee_btn = Button(self.frame1, text="ADMIN PORTAL", bd=0, bg='#ffffff', image=self.photo_employee,
                                   compound=TOP, command=self.employee)
        self.employee_btn.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.4)

    def student(self):
        self.frame.place_forget()
        student_menu = Login_Student.Student_Show(self.root, self.ls, self.frame)

    def employee(self):
        self.frame.place_forget()
        employee_menu = Login_Employee.Employee_Show(self.root, self.ls, self.frame)
'''
from tkinter import *
from tkinter import ttk

import Login_Student
import Login_Employee

class Main_Page:
    def __init__(self, root, ls):
        self.root = root
        self.ls = ls
        # Creating the first frame.
        self.frame = Frame(root)  # No need to specify background color for transparency
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Inserting TVS logo image
        self.tvs_logo = PhotoImage(file="Images/tvs.png")
        self.logo_label = Label(self.frame, image=self.tvs_logo)
        self.logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centering the logo

        # Creating the main frame.
        self.frame1 = Frame(self.frame, bg='#ffffff')
        self.frame1.place(x=ls[0]//9*2, y=ls[1]//4, width=ls[0]//9*5, height=ls[1]//4*2)

        # Taking All pics in the variable.
        self.photo_student = PhotoImage(file=r"Images/customer.png")
        self.photo_employee = PhotoImage(file=r"Images/admin.png")

        # Resizing the Images as per requirement.
        self.photo_student = self.photo_student.subsample(4, 4)
        self.photo_employee = self.photo_employee.subsample(4, 4)

        # Labeling the page.
        self.title1 = Label(self.frame1, text='TVS HOMEPAGE', font=('Algerian', 25, 'bold'), bg='#ffffff').pack(side=TOP)

        # Creating two buttons.
        self.student_btn = Button(self.frame1, text='CUSTOMER PORTAL', bd=0, bg='#ffffff', image=self.photo_student,
                                   compound=TOP, command=self.student) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9)*3-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)
        self.employee_btn = Button(self.frame1, text="ADMIN PORTAL", bd=0, bg='#ffffff', image=self.photo_employee,
                                   compound=TOP, command=self.employee) \
            .place(width=ls[0] // 9, height=ls[1] // 3, x=(ls[0]//9 * 5)-ls[0]//9*2, y=(ls[1] // 3)-ls[1]//4)

    def student(self):
        self.frame.place_forget()
        student_menu = Login_Student.Student_Show(self.root, self.ls, self.frame)

    def employee(self):
        self.frame.place_forget()
        employee_menu = Login_Employee.Employee_Show(self.root, self.ls, self.frame)
        
if __name__ == '__main__':
    # Getting the screensize in list.
    ls = list([1336, 714])
    print(ls)
    # Creating a fixed window.
    root = Tk()

    # Creating a bit icon.
    root.iconbitmap('icon.ico')

    # Title and Screen Setting.
    root.title("TVS Motors")  # Sets-up the title of the window.
    root.geometry(f"{ls[0]}x{ls[1]}+0+0")  # Width Height Left-padding Top-padding.
    root.minsize(ls[0], ls[1])  # Locking min-sized window.
    root.maxsize(ls[0], ls[1])  # Locking max-sized window.
    
    # Inserting TVS background image
    tvs_bg = PhotoImage(file="Images/tvs_bg.png")
    bg_label = Label(root, image=tvs_bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Starting the main window.
    firster = Main_Page(root, ls)

    # Starting a main window.
    root.mainloop()
