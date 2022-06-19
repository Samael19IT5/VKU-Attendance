import csv
import tkinter as tk
import os
import Menu as m3
from tkinter import ttk, filedialog
from tkinter import messagebox

from ConnectDatabase import getUser, listAttendance, fixAttendance, isLessonLecturer, deleteAttendance, searchAttendance
from Session import dateTime, getSession

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Attend(tk.Tk):
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

        background_img = tk.PhotoImage(file=dirGUI + "bgAttend.png")
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
            x=268, y=646,
            width=100,
            height=50)

        self.entry0 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry0.place(
            x=180, y=462,
            width=260,
            height=38)

        self.entry1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry1.place(
            x=180, y=523,
            width=260,
            height=38)

        self.entry2 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry2.place(
            x=180, y=583,
            width=260,
            height=38)

        self.entry3 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry3.place(
            x=180, y=402,
            width=260,
            height=38)

        self.entry4 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry4.place(
            x=180, y=342,
            width=260,
            height=38)

        self.entry5 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry5.place(
            x=180, y=282,
            width=260,
            height=38)

        self.entry6 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry6.place(
            x=180, y=166,
            width=260,
            height=38)

        self.entry7 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            state='disabled',
            highlightthickness=0)

        self.entry7.place(
            x=180, y=222,
            width=260,
            height=38)

        img2 = tk.PhotoImage(file=dirGUI + "btnAttendM.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnAttend,
            relief="flat")

        b2.place(
            x=32, y=646,
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
            x=150, y=646,
            width=100,
            height=50)

        img4 = tk.PhotoImage(file=dirGUI + "btnExportM.png")
        b4 = tk.Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnExport,
            relief="flat")

        b4.place(
            x=386, y=646,
            width=100,
            height=50)

        options = ['ID', 'ID Student', 'Student', 'Subject', 'Time', 'Date', 'Attend', 'ID Lesson']
        self.clicked = tk.StringVar()
        self.clicked.set(options[0])

        entry8 = tk.OptionMenu(self, self.clicked, *options)

        entry8.place(
            x=670, y=117,
            width=182,
            height=37)

        self.entry9 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry9.place(
            x=864, y=117,
            width=257,
            height=37)

        img5 = tk.PhotoImage(file=dirGUI + "btnSearch.png")
        b5 = tk.Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnSearch,
            relief="flat")

        b5.place(
            x=1133, y=117,
            width=56,
            height=39)

        img6 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b6 = tk.Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadAttendance,
            relief="flat")

        b6.place(
            x=1200, y=117,
            width=56,
            height=39)

        columns = ('ID', 'ID Student', 'Student', 'Subject', 'Time', 'Date', 'Attend', 'ID Lesson')

        self.b7 = ttk.Treeview(self, columns=columns, show='headings')
        self.b7.heading('ID', text='ID')
        self.b7.column('ID', width=40, anchor=tk.CENTER)
        self.b7.heading('ID Student', text='ID Student')
        self.b7.column('ID Student', width=70, anchor=tk.CENTER)
        self.b7.heading('Student', text='Student')
        self.b7.column('Student', width=110, anchor=tk.W)
        self.b7.heading('Subject', text='Subject')
        self.b7.column('Subject', width=150, anchor=tk.W)
        self.b7.heading('Time', text='Time')
        self.b7.column('Time', width=110, anchor=tk.CENTER)
        self.b7.heading('Date', text='Date')
        self.b7.column('Date', width=80, anchor=tk.CENTER)
        self.b7.heading('Attend', text='Attend')
        self.b7.column('Attend', width=110, anchor=tk.W)
        self.b7.heading('ID Lesson', text='ID Lesson')
        self.b7.column('ID Lesson', width=60, anchor=tk.CENTER)

        self.b7.bind('<<TreeviewSelect>>', self.itemSelect)

        self.b7.place(
            x=520, y=166,
            width=736,
            height=530)

        self.role = getSession()[-1]
        self.userID = getUser()[0]
        self.tick = None
        self.clock()
        self.loadAttendance()
        self.title('VKU Attendance')
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m3.Menu()

    def btnAttend(self):
        if self.entry6.get() != '':
            if self.entry1.get().strip() == 'Absent':
                if self.role == 'A' or self.role == 'L' and isLessonLecturer(self.entry2.get().strip(), self.userID):
                    fixAttendance(self.entry6.get().strip())
                    self.btnReset()
                    self.loadAttendance()
                    messagebox.showinfo('Success', 'Attend success!')
                else:
                    messagebox.showinfo('Attend failed', 'You not lecture this lesson!')
            else:
                messagebox.showinfo('Unsuitable', 'Please choose an absent attendance in list!')
        else:
            messagebox.showinfo('Empty entries', 'Please choose an attendance in list first!')

    def btnDelete(self):
        if self.entry6.get() != '':
            if self.role == 'A' or self.role == 'L' and isLessonLecturer(self.entry2.get().strip(), self.userID):
                ask = messagebox.askquestion('Delete attendance', 'Are you sure to delete this attendance?',
                                             icon='warning')
                if ask == 'yes':
                    deleteAttendance(self.entry6.get().strip())
                    self.btnReset()
                    self.loadAttendance()
                    messagebox.showinfo('Success', 'Delete success!')
            else:
                messagebox.showinfo('Delete failed', 'You not lecture this lesson!')
        else:
            messagebox.showinfo('Empty entries', 'Please choose an attendance in list first!')

    def btnReset(self):
        self.entry0.configure(state='normal')  # date
        setEntry(self.entry0, '')
        self.entry0.configure(state='disabled')
        self.entry1.configure(state='normal')  # attend
        setEntry(self.entry1, '')
        self.entry1.configure(state='disabled')
        self.entry2.configure(state='normal')  # id lesson
        setEntry(self.entry2, '')
        self.entry2.configure(state='disabled')
        self.entry3.configure(state='normal')  # time
        setEntry(self.entry3, '')
        self.entry3.configure(state='disabled')
        self.entry4.configure(state='normal')  # subject
        setEntry(self.entry4, '')
        self.entry4.configure(state='disabled')
        self.entry5.configure(state='normal')  # student
        setEntry(self.entry5, '')
        self.entry5.configure(state='disabled')
        self.entry6.configure(state='normal')  # id
        setEntry(self.entry6, '')
        self.entry6.configure(state='disabled')
        self.entry7.configure(state='normal')  # id student
        setEntry(self.entry7, '')
        self.entry7.configure(state='disabled')

    def btnExport(self):
        if len(self.b7.get_children()) > 0:
            file = filedialog.asksaveasfilename(defaultextension='.csv', initialdir=dir, title='Export File',
                                                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            if file != '':
                with open(file, mode='w', newline='', encoding='utf-8') as myFile:
                    exp = csv.writer(myFile, delimiter='\t')
                    for i in self.b7.get_children():
                        row = self.b7.item(i)['values']
                        exp.writerow(row)
                messagebox.showinfo('Success', 'Export success!')
        else:
            messagebox.showinfo('Empty value', 'There no values to export!')

    def loadAttendance(self):
        for item in self.b7.get_children():
            self.b7.delete(item)
        list = listAttendance()
        for x in list:
            self.b7.insert('', tk.END, values=x)

    def btnSearch(self):
        value = self.entry9.get()
        if value != '':
            col = self.clicked.get()
            for item in self.b7.get_children():
                self.b7.delete(item)
            list = searchAttendance(col, value)
            for x in list:
                self.b7.insert('', tk.END, values=x)
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry!")

    def clock(self):
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def itemSelect(self, _):
        for s in self.b7.selection():
            item = self.b7.item(s)
            attend = item['values']
            self.entry0.configure(state='normal')  # date
            setEntry(self.entry0, ' ' + attend[5])
            self.entry0.configure(state='disabled')
            self.entry1.configure(state='normal')  # attend
            setEntry(self.entry1, ' ' + attend[6])
            self.entry1.configure(state='disabled')
            self.entry2.configure(state='normal')  # id lesson
            setEntry(self.entry2, ' ' + str(attend[7]))
            self.entry2.configure(state='disabled')
            self.entry3.configure(state='normal')  # time
            setEntry(self.entry3, ' ' + attend[4])
            self.entry3.configure(state='disabled')
            self.entry4.configure(state='normal')  # subject
            setEntry(self.entry4, ' ' + attend[3])
            self.entry4.configure(state='disabled')
            self.entry5.configure(state='normal')  # student
            setEntry(self.entry5, ' ' + attend[2])
            self.entry5.configure(state='disabled')
            self.entry6.configure(state='normal')  # id
            setEntry(self.entry6, ' ' + str(attend[0]))
            self.entry6.configure(state='disabled')
            self.entry7.configure(state='normal')  # id student
            setEntry(self.entry7, ' ' + str(attend[1]))
            self.entry7.configure(state='disabled')
