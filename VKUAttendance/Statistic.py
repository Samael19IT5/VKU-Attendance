import csv
import tkinter as tk
import os
import Menu as m5

from tkinter import ttk, filedialog
from tkinter import messagebox

from ConnectDatabase import listStudent, listAttendance, listStatistic, searchStatistic, searchStatus
from Session import dateTime, getSession

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Statistic(tk.Tk):
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

        background_img = tk.PhotoImage(file=dirGUI + "bgStatistic.png")
        self.canvas.create_image(
            640.0, 176.0,
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

        img1 = tk.PhotoImage(file=dirGUI + "btnExport.png")
        b1 = tk.Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnExport,
            relief="flat")

        b1.place(
            x=941, y=609,
            width=216,
            height=50)

        self.entry0 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry0.place(
            x=1107, y=321,
            width=153,
            height=37)

        optionsColumn = ["ID", "Name", "Date", "Subject", "ID Lesson", "Status"]
        self.clickedColumn = tk.StringVar()
        self.clickedColumn.set(optionsColumn[0])

        entry1 = tk.OptionMenu(self, self.clickedColumn, *optionsColumn)

        entry1.place(
            x=943, y=321,
            width=153,
            height=37)

        optionsStatus = ["All", "Present", "Late", "Absent", "Present(X)", "Present-Present(X)", "Late-Absent"]
        self.clickedStatus = tk.StringVar()
        self.clickedStatus.set(optionsStatus[0])
        self.clickedStatus.trace("w", self.statusSelect)

        entry2 = tk.OptionMenu(self, self.clickedStatus, *optionsStatus)

        entry2.place(
            x=943, y=375,
            width=153,
            height=37)

        img2 = tk.PhotoImage(file=dirGUI + "btnSearch.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnSearch,
            relief="flat")

        b2.place(
            x=1109, y=375,
            width=56,
            height=39)

        img3 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b3 = tk.Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadListStatistic,
            relief="flat")

        b3.place(
            x=1178, y=375,
            width=56,
            height=39)

        columns = ('ID', 'Name', 'Date', 'Subject', 'ID Lesson', 'Status')

        self.b4 = ttk.Treeview(self, columns=columns, show='headings')
        self.b4.heading('ID', text='ID')
        self.b4.column('ID', width=50, anchor=tk.CENTER)
        self.b4.heading('Name', text='Name')
        self.b4.column('Name', width=150, anchor=tk.W)
        self.b4.heading('Date', text='Date')
        self.b4.column('Date', width=100, anchor=tk.W)
        self.b4.heading('Subject', text='Subject')
        self.b4.column('Subject', width=150, anchor=tk.W)
        self.b4.heading('ID Lesson', text='ID Lesson')
        self.b4.column('ID Lesson', width=100, anchor=tk.CENTER)
        self.b4.heading('Status', text='Status')
        self.b4.column('Status', width=120, anchor=tk.W)

        self.b4.place(
            x=14, y=321,
            width=788,
            height=385)

        self.b5 = tk.Label(
            bg='#374F8A',
            fg='white',
            anchor=tk.W,
            borderwidth=0,
            highlightthickness=0,
            font=("Inter", 18, 'bold'),
            relief="flat")

        self.b5.place(
            x=112, y=196,
            width=184,
            height=38)

        self.b6 = tk.Label(
            bg='#3FC1A5',
            fg='white',
            anchor=tk.W,
            borderwidth=0,
            highlightthickness=0,
            font=("Inter", 18, 'bold'),
            relief="flat")

        self.b6.place(
            x=409, y=196,
            width=209,
            height=38)

        self.b7 = tk.Label(
            bg='#F7961E',
            fg='white',
            anchor=tk.W,
            borderwidth=0,
            highlightthickness=0,
            font=("Inter", 18, 'bold'),
            relief="flat")

        self.b7.place(
            x=734, y=196,
            width=198,
            height=38)

        self.b8 = tk.Label(
            bg='#C82032',
            fg='white',
            anchor=tk.W,
            borderwidth=0,
            highlightthickness=0,
            font=("Inter", 18, 'bold'),
            relief="flat")

        self.b8.place(
            x=1044, y=196,
            width=198,
            height=38)

        self.tick = None
        self.clock()
        self.loadStatistic()
        self.loadListStatistic()
        self.title('VKU Attendance')
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m5.Menu()

    def btnExport(self):
        if len(self.b4.get_children()) > 0:
            file = filedialog.asksaveasfilename(defaultextension='.csv', initialdir=dir, title='Export File',
                                                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            if file != '':
                with open(file, mode='w', newline='', encoding='utf-8') as myFile:
                    exp = csv.writer(myFile, delimiter='\t')
                    for i in self.b4.get_children():
                        row = self.b4.item(i)['values']
                        exp.writerow(row)
                messagebox.showinfo('Success', 'Export success!')
        else:
            messagebox.showinfo('Empty value', 'There no values to export!')

    def loadStatistic(self):
        students = len(listStudent())
        self.b5.configure(text=students)
        attendances = listAttendance()
        self.b6.configure(text=len(attendances))
        late = 0
        absent = 0
        for i in attendances:
            if 'Late' in i[6]:
                late += 1
            elif 'Absent' in i[6]:
                absent += 1
        self.b7.configure(text=late)
        self.b8.configure(text=absent)

    def btnSearch(self):
        value = self.entry0.get()
        if value != '':
            col = self.clickedColumn.get()
            status = self.clickedStatus.get()
            for item in self.b4.get_children():
                self.b4.delete(item)
            list = searchStatistic(col, status, value)
            for x in list:
                self.b4.insert('', tk.END, values=x)
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry!")

    def clock(self):
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def loadListStatistic(self):
        for item in self.b4.get_children():
            self.b4.delete(item)
        list = listStatistic()
        for x in list:
            self.b4.insert('', tk.END, values=x)

    def statusSelect(self, *_):
        for item in self.b4.get_children():
            self.b4.delete(item)
        list = searchStatus(listStatistic(), self.clickedStatus.get())
        for x in list:
            self.b4.insert('', tk.END, values=x)
