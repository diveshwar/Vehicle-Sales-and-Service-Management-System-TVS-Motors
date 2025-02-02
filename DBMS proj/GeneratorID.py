from tkinter import *
from tkinter import ttk

import mysql.connector



class Class_ID:
    def __init__(self, root, ls, frame_old, roll):
        self.ls = ls
        self.root = root
        self.roll = roll
        self.frame_old = frame_old
        self.Roll_No_var = StringVar()

        # Creating the first Frame.
        self.frame = Frame(root, bg='#163148')
        self.frame.place(x=0, y=0, width=ls[0], height=ls[1])

        # Creating a back button.
        exit = Button(self.frame, text="Back", relief=RAISED, bg='#fbf8e6', command=self.exiting)
        exit.place(x=10, y=10, width=100, height=40)

        # Labeling the title
        title = Label(self.frame, text='ID GENERATOR', font=('Algerian', 25, 'bold'),
                      bg='lightgreen').pack(side=TOP)
        conn=mysql.connector.connect(host="localhost",user="root",passwd='79sumathi',database="tv")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student_data where Roll_No= " + str(self.roll))

        rows = cur.fetchall()

        self.name = str(rows[0][1])
        self.email = str(rows[0][2])
        self.gender = str(rows[0][3])
        self.phone = str(rows[0][4])
        self.dob = str(rows[0][5])
        self.address = str(rows[0][6])

        # Generating Bar Code.
        from PIL import Image, ImageDraw, ImageFont
        image = Image.new('RGB', (1000, 600), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype('arial.ttf', size=45)
        import qrcode

        # College Tag
        (x, y) = (230, 40)
        message = "TVD UNIVERSITY"
        company = message
        color = 'rgb(0, 0, 0)'
        font = ImageFont.truetype('arial.ttf', size=70)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 190)
        message = "Name: " + self.name
        company2 = message
        color = 'rgb(0, 0, 0)'  
        font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 260)
        message = "Gender: " + self.gender
        company3 = message
        color = 'rgb(0, 0, 0)'  
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 330)
        message = "Phone: " + self.phone
        company4 = message
        color = 'rgb(0, 0, 0)'  
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 400)
        message = "DOB: " + self.dob
        company5 = message
        color = 'rgb(0, 0, 0)'  
        draw.text((x, y), message, fill=color, font=font)

        (x, y) = (50, 470)
        message = "Location: " + self.address
        company6 = message
        color = 'rgb(0, 0, 0)'  
        draw.text((x, y), message, fill=color, font=font)

        

        image.save(str("id_card") + '.png')

        img = qrcode.make(str(company) + "\n"+str(company2)+ "\n"+str(company3)+ "\n"+str(company4)+ "\n"+str(company5)+ "\n"+str(company6))  #TO ADD INTO QR CODE
        img.save(str("id_card") + '.bmp')

        til = Image.open(str("id_card") + '.png')
        im = Image.open(str("id_card") + '.bmp')
        til.paste(im, (475, 120))
        til.save(str("id_card") + '.png')

        self.photo_ID_Card = PhotoImage(file=r"id_card.png").subsample(2,2)

        image_id = Label(self.frame, image=self.photo_ID_Card, bg="white")
        image_id.place(x=ls[0]*420//1336, y=ls[1]*260//714)

    def exiting(self):
        self.frame.destroy()
        self.root.title("vehicle Management System")
        self.frame_old.place(x=0, y=0, width=self.ls[0], height=self.ls[1])

