import tkinter as tk
import os
import Menu as m4
from tkinter import ttk
from tkinter import messagebox
from ConnectDatabase import addSubject, lectureSubject, renameSubject, quitSubject, deleteSubject, listSubject, \
    searchSubject, listLecturerSubject, searchLectureSubject, listStudentSubject, learnSubject, expelSubject, \
    searchStudentSubject

from ConnectDatabase import getUser
from Session import dateTime, getSession

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Subject(tk.Tk):
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

        background_img = tk.PhotoImage(file=dirGUI + "bgSubject.png")
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

        img1 = tk.PhotoImage(file=dirGUI + "btnResetM.png")
        b1 = tk.Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnReset,
            relief="flat")

        b1.place(
            x=516, y=354,
            width=100,
            height=50)

        self.entry0 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(16.0)))

        self.entry0.place(
            x=232, y=282,
            width=260,
            height=38)

        self.entry1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(16.0)))

        self.entry1.place(
            x=232, y=166,
            width=260,
            height=38)

        self.entry2 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry2.place(
            x=232, y=222,
            width=260,
            height=38)

        img2 = tk.PhotoImage(file=dirGUI + "btnLecture.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLecture,
            relief="flat")

        b2.place(
            x=516, y=192,
            width=100,
            height=50)

        img3 = tk.PhotoImage(file=dirGUI + "btnQuit.png")
        b3 = tk.Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnQuit,
            relief="flat")

        b3.place(
            x=516, y=257,
            width=100,
            height=50)

        img4 = tk.PhotoImage(file=dirGUI + "btnRename.png")
        b4 = tk.Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnRename,
            relief="flat")

        b4.place(
            x=230, y=354,
            width=100,
            height=50)

        optionsSubject = ["ID", "Name"]
        self.clickedSubject = tk.StringVar()
        self.clickedSubject.set(optionsSubject[0])

        entry3 = tk.OptionMenu(self, self.clickedSubject, *optionsSubject)

        entry3.place(
            x=805, y=116,
            width=153,
            height=33)

        optionsLecturer = ["ID", "Name", "Lecture"]
        self.clickedLecturer = tk.StringVar()
        self.clickedLecturer.set(optionsLecturer[0])

        entry4 = tk.OptionMenu(self, self.clickedLecturer, *optionsLecturer)

        entry4.place(
            x=296, y=431,
            width=80,
            height=37)

        optionsStudent = ["ID", "Name", "Learn"]
        self.clickedStudent = tk.StringVar()
        self.clickedStudent.set(optionsStudent[0])

        entry5 = tk.OptionMenu(self, self.clickedStudent, *optionsStudent)

        entry5.place(
            x=934, y=431,
            width=80,
            height=37)

        self.entry6 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(12.0)))

        self.entry6.place(
            x=389, y=431,
            width=103,
            height=37)

        self.entry7 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(12.0)))

        self.entry7.place(
            x=1027, y=431,
            width=103,
            height=37)

        self.entry8 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(12.0)))

        self.entry8.place(
            x=972, y=116,
            width=153,
            height=33)

        img5 = tk.PhotoImage(file=dirGUI + "btnSearch.png")
        b5 = tk.Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnSearch,
            relief="flat")

        b5.place(
            x=1139, y=116,
            width=56,
            height=39)

        img6 = tk.PhotoImage(file=dirGUI + "btnSearch.png")
        b6 = tk.Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLectureSearch,
            relief="flat")

        b6.place(
            x=503, y=431,
            width=56,
            height=39)

        img7 = tk.PhotoImage(file=dirGUI + "btnSearch.png")
        b7 = tk.Button(
            image=img7,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnStudentSearch,
            relief="flat")

        b7.place(
            x=1138, y=431,
            width=56,
            height=39)

        img8 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b8 = tk.Button(
            image=img8,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadSubject,
            relief="flat")

        b8.place(
            x=1204, y=116,
            width=56,
            height=39)

        img9 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b9 = tk.Button(
            image=img9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadLecturerSubject,
            relief="flat")

        b9.place(
            x=566, y=431,
            width=56,
            height=39)

        img10 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b10 = tk.Button(
            image=img10,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadStudentSubject,
            relief="flat")

        b10.place(
            x=1200, y=431,
            width=56,
            height=39)

        columnsSubject = ('ID', 'Name', 'No of Lecturers')

        self.b11 = ttk.Treeview(self, columns=columnsSubject, show='headings')
        self.b11.heading('ID', text='ID')
        self.b11.column('ID', width=50, anchor=tk.CENTER)
        self.b11.heading('Name', text='Name')
        self.b11.column('Name', width=300, anchor=tk.W)
        self.b11.heading('No of Lecturers', text='No of Lecturers')
        self.b11.column('No of Lecturers', width=50, anchor=tk.CENTER)

        self.b11.bind('<<TreeviewSelect>>', self.subjectSelect)

        self.b11.place(
            x=660, y=166,
            width=596,
            height=238)

        img12 = tk.PhotoImage(file=dirGUI + "btnAddM.png")
        b12 = tk.Button(
            image=img12,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnAdd,
            relief="flat")

        b12.place(
            x=87, y=354,
            width=100,
            height=50)

        img13 = tk.PhotoImage(file=dirGUI + "btnJoin.png")
        b13 = tk.Button(
            image=img13,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLecturerJoin,
            relief="flat")

        b13.place(
            x=46, y=622,
            width=100,
            height=50)

        img14 = tk.PhotoImage(file=dirGUI + "btnJoin.png")
        b14 = tk.Button(
            image=img14,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnStudentJoin,
            relief="flat")

        b14.place(
            x=679, y=622,
            width=100,
            height=50)

        columnsLecturer = ('ID', 'Name', 'Lecture')

        self.b15 = ttk.Treeview(self, columns=columnsLecturer, show='headings')

        self.b15.heading('ID', text='ID')
        self.b15.column('ID', width=50, anchor=tk.CENTER)
        self.b15.heading('Name', text='Name')
        self.b15.column('Name', width=150, anchor=tk.W)
        self.b15.heading('Lecture', text='Lecture')
        self.b15.column('Lecture', width=50, anchor=tk.CENTER)

        self.b15.bind('<<TreeviewSelect>>', self.lecturerSelect)

        self.b15.place(
            x=296, y=482,
            width=322,
            height=214)

        columnsStudent = ('ID', 'Name', 'Learn')

        self.b16 = ttk.Treeview(self, columns=columnsStudent, show='headings')

        self.b16.heading('ID', text='ID')
        self.b16.column('ID', width=50, anchor=tk.CENTER)
        self.b16.heading('Name', text='Name')
        self.b16.column('Name', width=150, anchor=tk.W)
        self.b16.heading('Learn', text='Learn')
        self.b16.column('Learn', width=50, anchor=tk.CENTER)

        self.b16.bind('<<TreeviewSelect>>', self.studentSelect)

        self.b16.place(
            x=934, y=482,
            width=322,
            height=214)

        self.entry9 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(12.0)))

        self.entry9.place(
            x=106, y=497,
            width=182,
            height=38)

        self.entry10 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(12.0)))

        self.entry10.place(
            x=745, y=497,
            width=182,
            height=38)

        self.entry11 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(12.0)))

        self.entry11.place(
            x=745, y=548,
            width=182,
            height=38)

        self.entry12 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(12.0)))

        self.entry12.place(
            x=106, y=548,
            width=182,
            height=38)

        img17 = tk.PhotoImage(file=dirGUI + "btnRemove.png")
        b17 = tk.Button(
            image=img17,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLecturerRemove,
            relief="flat")

        b17.place(
            x=168, y=622,
            width=100,
            height=50)

        img18 = tk.PhotoImage(file=dirGUI + "btnRemove.png")
        b18 = tk.Button(
            image=img18,
            borderwidth=0,
            command=self.btnStudentRemove,
            relief="flat")

        b18.place(
            x=801, y=622,
            width=100,
            height=50)

        img19 = tk.PhotoImage(file=dirGUI + "btnDeleteM.png")
        b19 = tk.Button(
            image=img19,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnDelete,
            relief="flat")

        b19.place(
            x=373, y=354,
            width=100,
            height=50)

        self.role = getSession()[-1]
        self.userID = getUser()[0]
        self.subjectID = None
        self.lecturerID = None
        self.lecture = None
        self.studentID = None
        self.learn = None
        self.tick = None
        self.loadSubject()
        self.clock()
        self.title("VKU Attendance")
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m4.Menu()

    def btnAdd(self):
        if self.entry0.get() == '' and self.entry1.get() == '':
            name = self.entry2.get()
            if name != '':
                addSubject(name)
                self.btnReset()
                self.loadSubject()
                messagebox.showinfo('Success', 'Add subject success!')
            else:
                messagebox.showinfo('Empty entry', 'Name entry is empty!')
        else:
            messagebox.showinfo('Reset ID', 'Please click Reset button first!')

    def btnLecture(self):
        if self.role == 'L':
            if self.entry1.get() != '':
                lectureSubject(self.entry1.get(), self.userID)
                self.btnReset()
                self.loadSubject()
                messagebox.showinfo('Success', 'Apply to lecture success!')
            else:
                messagebox.showinfo('ID entry empty', 'Please select subject in list first!')
        else:
            messagebox.showinfo('Function not suitable', 'This function is only use for Lecturer!')

    def btnRename(self):
        if self.entry1.get() != '':
            if renameSubject(self.entry1.get(), self.entry2.get()):
                self.btnReset()
                self.loadSubject()
                messagebox.showinfo('Success', 'Rename subject success!')
            else:
                messagebox.showinfo('Not rename', 'The set name is same as original!')
        else:
            messagebox.showinfo('ID entry empty', 'Please select subject in list first!')

    def btnDelete(self):
        if self.entry1.get() != '':
            ask = messagebox.askquestion('Delete subject', 'Are you sure to delete this subject?', icon='warning')
            if ask == 'yes':
                deleteSubject(self.entry1.get())
                self.btnReset()
                self.loadSubject()
                messagebox.showinfo('Success', "Delete subject success!")
        else:
            messagebox.showinfo('ID entry empty', 'Please select subject in list first!')

    def btnQuit(self):
        if self.role == 'L':
            if self.entry1.get() != '':
                if quitSubject(self.entry1.get(), self.userID):
                    self.btnReset()
                    self.loadSubject()
                    messagebox.showinfo('Success', 'Quit subject success!')
                else:
                    messagebox.showinfo('No lecture', 'You do not teach this subject!')
            else:
                messagebox.showinfo('ID entry empty', 'Please select subject in list first!')
        else:
            messagebox.showinfo('Function not suitable', 'This function is only use for Lecturer!')

    def btnReset(self):
        self.entry0.configure(state='normal')
        setEntry(self.entry0, '')
        self.entry0.configure(state='disabled')
        self.entry1.configure(state='normal')
        setEntry(self.entry1, '')
        self.entry1.configure(state='disabled')
        setEntry(self.entry2, '')
        self.entry9.configure(state='normal')
        setEntry(self.entry9, '')
        self.entry9.configure(state='disabled')
        self.entry10.configure(state='normal')
        setEntry(self.entry10, '')
        self.entry10.configure(state='disabled')
        self.entry11.configure(state='normal')
        setEntry(self.entry11, '')
        self.entry11.configure(state='disabled')
        self.entry12.configure(state='normal')
        setEntry(self.entry12, '')
        self.entry12.configure(state='disabled')
        self.subjectID = None
        self.lecturerID = None
        self.lecture = None
        self.studentID = None
        self.learn = None
        for item in self.b15.get_children():
            self.b15.delete(item)
        for item in self.b16.get_children():
            self.b16.delete(item)

    def loadSubject(self):
        for item in self.b11.get_children():
            self.b11.delete(item)
        list = listSubject()
        for x in list:
            self.b11.insert('', tk.END, values=x)

    def loadLecturerSubject(self):
        for item in self.b15.get_children():
            self.b15.delete(item)
        list = listLecturerSubject(self.subjectID)
        for x in list:
            self.b15.insert('', tk.END, values=x)

    def loadStudentSubject(self):
        for item in self.b16.get_children():
            self.b16.delete(item)
        list = listStudentSubject(self.subjectID)
        for x in list:
            self.b16.insert('', tk.END, values=x)

    def btnSearch(self):
        value = self.entry8.get()
        if value != '':
            col = self.clickedSubject.get()
            if col == "ID":
                col = "id"
            else:
                col = "name"
            for item in self.b11.get_children():
                self.b11.delete(item)
            list = searchSubject(col, value)
            for x in list:
                self.b11.insert('', tk.END, values=x)
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry!")

    def btnLectureSearch(self):
        value = self.entry6.get()
        if value != '' and self.subjectID is not None:
            col = self.clickedLecturer.get()
            if col == "ID":
                col = "id"
            elif col == "Name":
                col = "name"
            else:
                col = "Lecture"
            for item in self.b15.get_children():
                self.b15.delete(item)
            list = searchLectureSubject(col, value, self.subjectID)
            for x in list:
                self.b15.insert('', tk.END, values=x)
            self.lectureReset()
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry or select subject first!")

    def btnLecturerJoin(self):
        if self.role == 'A':
            if self.lecture == 'Yes':
                messagebox.showinfo("Not suitable", "This lecturer has already joined to this subject!")
            elif self.lecture == 'No':
                lectureSubject(self.subjectID, self.lecturerID)
                self.loadSubject()
                self.loadLecturerSubject()
                self.lectureReset()
                messagebox.showinfo("Success", "Lecturer joined to this subject!")
            else:
                messagebox.showinfo("Empty entry", "Please choose the lecturer in list first!")
        else:
            messagebox.showinfo('Insufficient permissions', 'This function is for admin only!')

    def btnLecturerRemove(self):
        if self.role == 'A':
            if self.lecture == 'No':
                messagebox.showinfo("Not suitable", "This lecturer not lecture this subject!")
            elif self.lecture == 'Yes':
                quitSubject(self.subjectID, self.lecturerID)
                self.loadSubject()
                self.loadLecturerSubject()
                self.lectureReset()
                messagebox.showinfo("Success", "Success remove this lecturer!")
            else:
                messagebox.showinfo("Empty entry", "Please choose the lecturer in list first!")
        else:
            messagebox.showinfo('Insufficient permissions', 'This function is for admin only!')

    def lectureReset(self):
        self.entry9.configure(state='normal')
        setEntry(self.entry9, '')
        self.entry9.configure(state='disabled')
        self.entry12.configure(state='normal')
        setEntry(self.entry12, '')
        self.entry12.configure(state='disabled')
        self.lecturerID = None
        self.lecture = None

    def btnStudentSearch(self):
        value = self.entry7.get()
        if value != '' and self.subjectID is not None:
            col = self.clickedStudent.get()
            if col == "ID":
                col = "id"
            elif col == "Name":
                col = "name"
            else:
                col = "Learn"
            for item in self.b16.get_children():
                self.b16.delete(item)
            list = searchStudentSubject(col, value, self.subjectID)
            for x in list:
                self.b16.insert('', tk.END, values=x)
            self.studentReset()
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry or select subject first!")

    def btnStudentJoin(self):
        if self.learn == 'Yes':
            messagebox.showinfo("Not suitable", "This student has already learnt this subject!")
        elif self.learn == 'No':
            learnSubject(self.subjectID, self.studentID)
            self.loadStudentSubject()
            self.studentReset()
            messagebox.showinfo("Success", "Student joined to this subject!")
        else:
            messagebox.showinfo("Empty entry", "Please choose the student in list first!")

    def btnStudentRemove(self):
        if self.learn == 'No':
            messagebox.showinfo("Not suitable", "This Student not learn this subject!")
        elif self.learn == 'Yes':
            expelSubject(self.subjectID, self.studentID)
            self.loadStudentSubject()
            self.studentReset()
            messagebox.showinfo("Success", "Success remove this student!")
        else:
            messagebox.showinfo("Empty entry", "Please choose the student in list first!")

    def studentReset(self):
        self.entry10.configure(state='normal')
        setEntry(self.entry10, '')
        self.entry10.configure(state='disabled')
        self.entry11.configure(state='normal')
        setEntry(self.entry11, '')
        self.entry11.configure(state='disabled')
        self.studentID = None
        self.learn = None

    def clock(self):
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def subjectSelect(self, _):
        for s in self.b11.selection():
            item = self.b11.item(s)
            subject = item['values']
            self.entry1.configure(state='normal')
            setEntry(self.entry1, subject[0])
            self.entry1.configure(state='disabled')
            setEntry(self.entry2, subject[1])
            self.entry0.configure(state='normal')
            setEntry(self.entry0, subject[2])
            self.entry0.configure(state='disabled')
            self.subjectID = subject[0]
            self.loadLecturerSubject()
            self.loadStudentSubject()

    def lecturerSelect(self, _):
        for s in self.b15.selection():
            item = self.b15.item(s)
            lecturer = item['values']
            self.entry9.configure(state='normal')
            setEntry(self.entry9, lecturer[0])
            self.entry9.configure(state='disabled')
            self.entry12.configure(state='normal')
            setEntry(self.entry12, lecturer[1])
            self.entry12.configure(state='disabled')
            self.lecturerID = lecturer[0]
            self.lecture = lecturer[2]

    def studentSelect(self, _):
        for s in self.b16.selection():
            item = self.b16.item(s)
            student = item['values']
            self.entry10.configure(state='normal')
            setEntry(self.entry10, student[0])
            self.entry10.configure(state='disabled')
            self.entry11.configure(state='normal')
            setEntry(self.entry11, student[1])
            self.entry11.configure(state='disabled')
            self.studentID = student[0]
            self.learn = student[2]
