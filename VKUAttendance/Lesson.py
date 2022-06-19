import tkinter as tk
import os
import Menu as m7
from tkinter import ttk
from tkinter import messagebox
from ConnectDatabase import getUser, addLesson, editLesson, deleteLesson, searchLesson, listLesson, listSubjectOptions
from Session import dateTime, getSession, compareTime, checkTime

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Lesson(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720+100+50")
        self.configure(bg="#ffffff")
        self.role = getSession()[-1]
        self.userID = getUser()[0]
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

        background_img = tk.PhotoImage(file=dirGUI + "bgLesson.png")
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
            x=404, y=540,
            width=100,
            height=50)

        if self.role == 'L':
            self.options = list(listSubjectOptions(self.userID))
        else:
            self.options = ['', '']
        self.clicked = tk.StringVar()
        self.clicked.set(self.options[0])

        self.entry0 = tk.OptionMenu(self, self.clicked, *self.options)

        self.entry0.place(
            x=232, y=462,
            width=260,
            height=38)

        self.entry1 = tk.Entry(  # lecturer
            bd=0,
            bg="#d9d9d9",
            state='disabled',
            font=("Inter-Regular", int(16.0)),
            highlightthickness=0)

        self.entry1.place(
            x=232, y=402,
            width=260,
            height=38)

        self.entry2 = tk.Entry(  # date
            bd=0,
            bg="#d9d9d9",
            state='disabled',
            font=("Inter-Regular", int(16.0)),
            highlightthickness=0)

        self.entry2.place(
            x=232, y=342,
            width=260,
            height=38)

        self.entry3 = tk.Entry(  # timeEnd
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(16.0)),
            highlightthickness=0)

        self.entry3.place(
            x=232, y=282,
            width=260,
            height=38)

        self.entry4 = tk.Entry(  # id
            bd=0,
            bg="#d9d9d9",
            state='disabled',
            font=("Inter-Regular", int(16.0)),
            highlightthickness=0)

        self.entry4.place(
            x=232, y=166,
            width=260,
            height=38)

        self.entry5 = tk.Entry(  # timeStart
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(16.0)),
            highlightthickness=0)

        self.entry5.place(
            x=232, y=222,
            width=260,
            height=38)

        img2 = tk.PhotoImage(file=dirGUI + "btnAddM.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnAdd,
            relief="flat")

        b2.place(
            x=29, y=540,
            width=100,
            height=50)

        img3 = tk.PhotoImage(file=dirGUI + "btnDeleteM.png")
        b3 = tk.Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnDelete,
            relief="flat")

        b3.place(
            x=279, y=540,
            width=100,
            height=50)

        img4 = tk.PhotoImage(file=dirGUI + "btnEditM.png")
        b4 = tk.Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnEdit,
            relief="flat")

        b4.place(
            x=154, y=540,
            width=100,
            height=50)

        searchOptions = ["ID", "Name", "Date", "Time Start", "Time End", "Lecturer", "You"]
        self.searchClicked = tk.StringVar()
        self.searchClicked.set(searchOptions[0])

        entry6 = ttk.OptionMenu(self, self.searchClicked, *searchOptions)

        entry6.place(
            x=725, y=116,
            width=174,
            height=37)

        self.entry7 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0)

        self.entry7.place(
            x=920, y=117,
            width=205,
            height=37)

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

        img6 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b6 = tk.Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadLesson,
            relief="flat")

        b6.place(
            x=1204, y=116,
            width=56,
            height=39)

        columns = ('ID', 'Name', 'Date', 'Time Start', 'Time End', 'Lecturer')

        self.b7 = ttk.Treeview(self, columns=columns, show='headings')

        self.b7.heading('ID', text='ID')
        self.b7.column('ID', width=50, anchor=tk.CENTER)
        self.b7.heading('Name', text='Name')
        self.b7.column('Name', width=200, anchor=tk.W)
        self.b7.heading('Date', text='Date')
        self.b7.column('Date', width=80, anchor=tk.W)
        self.b7.heading('Time Start', text='Time Start')
        self.b7.column('Time Start', width=80, anchor=tk.W)
        self.b7.heading('Time End', text='Time End')
        self.b7.column('Time End', width=80, anchor=tk.W)
        self.b7.heading('Lecturer', text='Lecturer')
        self.b7.column('Lecturer', width=150, anchor=tk.W)

        self.b7.bind('<<TreeviewSelect>>', self.itemSelect)

        self.b7.place(
            x=549, y=166,
            width=707,
            height=530)

        self.tick = None
        self.lecturerID = None
        self.clock()
        self.loadLesson()
        self.title('VKU Attendance')
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m7.Menu()

    def btnAdd(self):
        if self.role == 'L':
            if self.entry4.get() == '':
                end = self.entry3.get()
                start = self.entry5.get()
                subject = self.clicked.get()
                if all(v != '' for v in [start, end, subject]):
                    if compareTime(start, end):
                        addLesson(subject, self.userID, start, end)
                        self.btnReset()
                        self.loadLesson()
                        messagebox.showinfo('Success', 'Add lesson success!')
                    else:
                        messagebox.showinfo('Invalid time', 'A study session lasting at least 45 minutes!')
                else:
                    messagebox.showinfo('Empty entry', 'Please fill all entries!')
            else:
                messagebox.showinfo('Reset ID', 'Please click Reset button first!')
        else:
            messagebox.showinfo('Not usable', 'This function is for lecturer only!')

    def btnEdit(self):
        if self.role == 'L':
            if self.entry4.get() != '':
                if self.lecturerID == self.userID:
                    end = self.entry3.get()
                    start = self.entry5.get()
                    if all(v != '' for v in [start, end]):
                        if checkTime(start, end):
                            if compareTime(start, end):
                                editLesson(self.entry4.get(), start, end)
                                self.btnReset()
                                self.loadLesson()
                                messagebox.showinfo('Success', 'Edit lesson success!')
                            else:
                                messagebox.showinfo('Invalid time', 'A study session lasting at least 45 minutes!')
                        else:
                            messagebox.showinfo('Invalid time', 'The time set is invalid!')
                    else:
                        messagebox.showinfo('Empty entry', 'Please fill all entries!')
                else:
                    messagebox.showinfo('Not authorized', 'You can not edit lesson of other lecturers!')
            else:
                messagebox.showinfo('Empty ID', 'Please choose lesson from list!')
        else:
            messagebox.showinfo('Not usable', 'This function is for lecturer only!')

    def btnDelete(self):
        if self.role == 'L':
            id = self.entry4.get()
            if id != '':
                if self.lecturerID == self.userID:
                    ask = messagebox.askquestion('Delete lesson', 'Are you sure to delete this lesson?',
                                                 icon='warning')
                    if ask == 'yes':
                        deleteLesson(id)
                        self.btnReset()
                        self.loadLesson()
                        messagebox.showinfo('Success', "Delete lesson success!")
                else:
                    messagebox.showinfo('Not authorized', 'You can not delete lesson of other lecturers!')
            else:
                messagebox.showinfo('Not have ID', 'Please select lesson in list first!')
        else:
            messagebox.showinfo('Insufficient permissions', 'This function is for lecturer only!')

    def btnReset(self):
        self.entry0.configure(state='normal')
        self.clicked.set('')
        self.entry0['menu'].delete(0, 'end')
        for i in self.options:
            self.entry0['menu'].add_command(label=i, command=tk._setit(self.clicked, i))
        self.clicked.set(self.options[0])
        self.entry1.configure(state='normal')
        setEntry(self.entry1, '')
        self.entry1.configure(state='disabled')
        self.entry2.configure(state='normal')
        setEntry(self.entry2, '')
        self.entry2.configure(state='disabled')
        self.entry4.configure(state='normal')
        setEntry(self.entry4, '')
        self.entry4.configure(state='disabled')
        setEntry(self.entry3, '')
        setEntry(self.entry5, '')

    def btnSearch(self):
        value = self.entry7.get()
        col = self.searchClicked.get()
        if value != '':
            if col == "ID":
                col = "lesson.id"
            elif col == "Name":
                col = "subject.name"
            elif col == "Date":
                col = "date"
            elif col == "Time Start":
                col = "timeStart"
            elif col == "Time End":
                col = "timeEnd"
            elif col == "Lecturer":
                col = "lecturer.name"
            for item in self.b7.get_children():
                self.b7.delete(item)
            list = searchLesson(col, value)
            for x in list:
                self.b7.insert('', tk.END, values=x)
        else:
            if col == 'You':
                if self.role == 'L':
                    value = str(self.userID)
                    for item in self.b7.get_children():
                        self.b7.delete(item)
                    list = searchLesson(col, value)
                    for x in list:
                        self.b7.insert('', tk.END, values=x)
                else:
                    messagebox.showinfo("No result", "Can not show result because you not a lecturer!")
            else:
                messagebox.showinfo("Empty entry", "Please fill in entry!")

    def loadLesson(self):
        for item in self.b7.get_children():
            self.b7.delete(item)
        list = listLesson()
        for x in list:
            self.b7.insert('', tk.END, values=x)

    def clock(self):
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def itemSelect(self, _):
        for s in self.b7.selection():
            item = self.b7.item(s)
            lesson = item['values']
            options = [lesson[1], '']
            self.clicked.set('')
            self.entry0['menu'].delete(0, 'end')
            for i in options:
                self.entry0['menu'].add_command(label=i, command=tk._setit(self.clicked, i))
            self.clicked.set(options[0])
            self.entry0.configure(state='disabled')
            setEntry(self.entry5, lesson[3])
            setEntry(self.entry3, lesson[4])
            self.entry4.configure(state='normal')
            setEntry(self.entry4, lesson[0])
            self.entry4.configure(state='disabled')
            self.entry2.configure(state='normal')
            setEntry(self.entry2, lesson[2])
            self.entry2.configure(state='disabled')
            self.entry1.configure(state='normal')
            setEntry(self.entry1, lesson[5])
            self.entry1.configure(state='disabled')
            self.lecturerID = lesson[6]
