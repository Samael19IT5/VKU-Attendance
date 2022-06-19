import os
import tkinter as tk
import Menu as m1
import cv2
from Image import Image
from tkinter import ttk
from tkinter import messagebox
from Session import dateTime
from ConnectDatabase import addStudent, editStudent, deleteStudent, saveImageStudent, searchStudent, listStudent, \
    checkImage, deleteImage

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"
dirCascade = os.getcwd() + "\\cascade\\"
dirDataset = os.getcwd() + "\\dataset\\"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(dirCascade + "haarcascade_frontalface_default.xml")


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Student(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720+100+50")
        self.configure(bg="#ffffff")
        self.canvas = tk.Canvas(
            self,
            bg="#ffffff",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        icon = tk.PhotoImage(file=dirGUI + 'icon.png')
        self.iconphoto(False, icon)

        background_img = tk.PhotoImage(file=dirGUI + "bgStudent.png")
        self.canvas.create_image(
            638.5, 385.5,
            image=background_img)

        self.bTime = self.canvas.create_text(
            1170.0, 48.0,
            text="99:99:99 PM\n20-04-2021",
            fill="#000000",
            font=("Inter-Regular", int(24.0)))

        img0 = tk.PhotoImage(file=dirGUI + "btnLogout.png")
        b0 = tk.Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnBack,
            relief="flat")

        b0.place(
            x=14, y=13,
            width=65,
            height=65)

        img1 = tk.PhotoImage(file=dirGUI + "btnGetImage.png")
        b1 = tk.Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnGetImage,
            relief="flat")

        b1.place(
            x=66, y=640,
            width=216,
            height=50)

        img2 = tk.PhotoImage(file=dirGUI + "btnSaveImage.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnSaveImage,
            relief="flat")

        b2.place(
            x=354, y=640,
            width=216,
            height=50)

        img3 = tk.PhotoImage(file=dirGUI + "btnReset.png")
        b3 = tk.Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnReset,
            relief="flat")

        b3.place(
            x=474, y=565,
            width=120,
            height=50)

        self.entry0 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry0.place(
            x=232, y=462,
            width=260,
            height=39)

        self.entry1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry1.place(
            x=232, y=402,
            width=260,
            height=39)

        self.entry2 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry2.place(
            x=232, y=342,
            width=260,
            height=39)

        self.entry3 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry3.place(
            x=232, y=282,
            width=260,
            height=39)

        self.entry4 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(16.0)))

        self.entry4.place(
            x=232, y=166,
            width=260,
            height=39)

        self.entry5 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry5.place(
            x=232, y=222,
            width=260,
            height=39)

        img4 = tk.PhotoImage(file=dirGUI + "btnAdd.png")
        b4 = tk.Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnAdd,
            relief="flat")

        b4.place(
            x=42, y=565,
            width=120,
            height=50)

        img5 = tk.PhotoImage(file=dirGUI + "btnDelete.png")
        b5 = tk.Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnDelete,
            relief="flat")

        b5.place(
            x=330, y=565,
            width=120,
            height=50)

        img6 = tk.PhotoImage(file=dirGUI + "btnEdit.png")
        b6 = tk.Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnEdit,
            relief="flat")

        b6.place(
            x=186, y=565,
            width=120,
            height=50)

        options = ["ID", "Name", "Class", "Student ID", "Phone", "Email"]
        self.clicked = tk.StringVar()
        self.clicked.set(options[0])

        entry6 = tk.OptionMenu(self, self.clicked, *options)

        entry6.place(
            x=805, y=116,
            width=153,
            height=40)

        self.entry7 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(12.0)))

        self.entry7.place(
            x=972, y=117,
            width=153,
            height=37)

        img7 = tk.PhotoImage(file=dirGUI + "btnSearch.png")
        b7 = tk.Button(
            image=img7,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnSearch,
            relief="flat")

        b7.place(
            x=1139, y=116,
            width=56,
            height=39)

        img8 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b8 = tk.Button(
            image=img8,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadStudent,
            relief="flat")

        b8.place(
            x=1204, y=116,
            width=56,
            height=39)

        columns = ('ID', 'Name', 'Class', 'SID', 'Phone', 'Email')
        self.b9 = ttk.Treeview(self, columns=columns, show='headings')
        self.b9.heading('ID', text='ID')
        self.b9.column('ID', width=50, anchor=tk.CENTER)
        self.b9.heading('Name', text='Name')
        self.b9.column('Name', width=150, anchor=tk.W)
        self.b9.heading('Class', text='Class')
        self.b9.column('Class', width=50, anchor=tk.W)
        self.b9.heading('SID', text='SID')
        self.b9.column('SID', width=50, anchor=tk.W)
        self.b9.heading('Phone', text='Phone')
        self.b9.column('Phone', width=80, anchor=tk.W)
        self.b9.heading('Email', text='Email')
        self.b9.column('Email', width=150, anchor=tk.W)

        self.b9.bind('<<TreeviewSelect>>', self.itemSelect)

        self.b9.place(
            x=660, y=166,
            width=596,
            height=530)

        self.tick = None
        self.loadStudent()
        self.clock()
        self.title("VKU Attendance")
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m1.Menu()

    def btnAdd(self):
        if self.entry4.get() == '':
            name = self.entry5.get()
            classS = self.entry3.get()
            studentID = self.entry2.get()
            phone = self.entry1.get()
            email = self.entry0.get()
            if all(v != '' for v in [name, classS, studentID, phone, email]):
                addStudent(name, classS, studentID, phone, email)
                self.btnReset()
                self.loadStudent()
                messagebox.showinfo('Success', 'Add student success!')
            else:
                messagebox.showinfo('Empty entry', 'Please fill all entries!')
        else:
            messagebox.showinfo('Reset ID', 'Please click Reset button first!')

    def btnEdit(self):
        id = self.entry4.get()
        if id != '':
            name = self.entry5.get()
            classS = self.entry3.get()
            studentID = self.entry2.get()
            phone = self.entry1.get()
            email = self.entry0.get()
            if all(v != '' for v in [name, classS, studentID, phone, email]):
                editStudent(id, name, classS, studentID, phone, email)
                self.btnReset()
                self.loadStudent()
                messagebox.showinfo('Success', 'Edit student success!')
            else:
                messagebox.showinfo('Empty entry', 'Please fill all entries!')
        else:
            messagebox.showinfo('Not have ID', 'Please select student in list first!')

    def btnDelete(self):
        id = self.entry4.get()
        if id != '':
            ask = messagebox.askquestion('Delete student', 'Are you sure to delete this student?', icon='warning')
            if ask == 'yes':
                deleteStudent(id)
                self.btnReset()
                self.loadStudent()
                messagebox.showinfo('Success', "Delete student success!")
        else:
            messagebox.showinfo('Not have ID', 'Please select student in list first!')

    def btnReset(self):
        setEntry(self.entry0, '')
        setEntry(self.entry1, '')
        setEntry(self.entry2, '')
        setEntry(self.entry3, '')
        self.entry4.configure(state='normal')
        setEntry(self.entry4, '')
        self.entry4.configure(state='disabled')
        setEntry(self.entry5, '')

    def btnGetImage(self):
        id = self.entry4.get()
        if id != '':
            Image(id)
        else:
            messagebox.showinfo('Not have ID', 'Please select student in list first!')

    def btnSaveImage(self):
        id = self.entry4.get()
        if id != '':
            ck = True
            for i in range(1, 31):
                if not os.path.exists(dirDataset + str(id) + "-" + str(i) + ".png"):
                    ck = False
            if ck:
                if checkImage(id):
                    deleteImage(id)
                saveImageStudent(id)
                messagebox.showinfo('Success', 'Save student images success!')
            else:
                messagebox.showinfo('Missing images', 'Please capture images first!')
        else:
            messagebox.showinfo('Not have ID', 'Please select student in list first!')

    def btnSearch(self):
        value = self.entry7.get()
        if value != '':
            col = self.clicked.get()
            if col == "ID":
                col = "id"
            elif col == "Name":
                col = "name"
            elif col == "Student ID":
                col = "code"
            elif col == "Phone":
                col = "phone"
            else:
                col = "email"
            for item in self.b9.get_children():
                self.b9.delete(item)
            list = searchStudent(col, value)
            for x in list:
                self.b9.insert('', tk.END, values=x)
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry!")

    def loadStudent(self):
        for item in self.b9.get_children():
            self.b9.delete(item)
        list = listStudent()
        for x in list:
            self.b9.insert('', tk.END, values=x)

    def clock(self):
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def itemSelect(self, _):
        for s in self.b9.selection():
            item = self.b9.item(s)
            student = item['values']
            self.entry4.configure(state='normal')
            setEntry(self.entry4, student[0])
            self.entry4.configure(state='disabled')
            setEntry(self.entry5, student[1])
            setEntry(self.entry3, student[2])
            setEntry(self.entry2, student[3])
            setEntry(self.entry1, student[4])
            setEntry(self.entry0, student[5])
