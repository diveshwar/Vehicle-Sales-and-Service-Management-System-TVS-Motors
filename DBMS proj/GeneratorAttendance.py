from tkinter import *
from tkinter import ttk

import mysql.connector

class Class_Attendance:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.frame_old = frame_old
        self.roll = roll
        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='ATTENDENCE CALCULATOR', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)

        conn=mysql.connector.connect(host="localhost",user="root",passwd='',database="tv")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.roll))

        rows = cur.fetchall()
        if len(rows) != 0:
            self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
            self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)

            cur.execute("SELECT * FROM student_attendance where Roll_No= " + str(self.roll))
            rows_attendence_roll = cur.fetchall()
            if len(rows_attendence_roll) != 0 and int(rows_attendence_roll[0][2]) != 0:
                self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
                self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)
                percentage = int(rows_attendence_roll[0][1])/int(rows_attendence_roll[0][2])*100

                # Labeling And Roll_No
                lbl_roll = Label(self.Detail_Frame, text=f"Your Attendence is {percentage}%!!!", bg="cornsilk",
                                 fg="blue",
                                 font=("times new roman", 30, "bold"))
                lbl_roll.pack(fill=BOTH, expand=1, anchor=CENTER)
            else:
                self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
                self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)

                # Labeling And Roll_No
                lbl_roll = Label(self.Detail_Frame, text="NO DATA PRESENT FOR THIS STUDENT", bg="cornsilk",
                                 fg="blue",
                                 font=("times new roman", 30, "bold"))
                lbl_roll.pack(fill=BOTH, expand=1, anchor=CENTER)

        else:
            self.Detail_Frame = Frame(self.frame, bd=4, relief=RIDGE, bg="cornsilk")
            self.Detail_Frame.place(x=ls[0]*240//1336, y=ls[1]*300//714, width=ls[0]*830//1336, height=ls[1]*280//714)

            # Labeling And Roll_No
            lbl_roll = Label(self.Detail_Frame, text="NO STUDENT EXISTS", bg="cornsilk", fg="blue",
                             font=("times new roman", 30, "bold"))
            lbl_roll.pack(fill=BOTH, expand=1, anchor=CENTER)
        pass

    def exiting(self):
        self.frame.destroy()
        self.root.title("vehicle Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

