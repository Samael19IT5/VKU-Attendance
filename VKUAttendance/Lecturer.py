import tkinter as tk
import os
import Menu as m6
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from Session import dateTime, getSession
from ConnectDatabase import getUser, addLecturer, editLecturer, deleteLecturer, listLecturer, searchLecturer

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


class Lecturer(tk.Tk):
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

        background_img = tk.PhotoImage(file=dirGUI + "bgLecturer.png")
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

        img1 = tk.PhotoImage(file=dirGUI + "btnReset.png")
        b1 = tk.Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnReset,
            relief="flat")

        b1.place(
            x=474, y=565,
            width=120,
            height=50)

        self.entry0 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry0.place(
            x=232, y=402,
            width=260,
            height=38)

        self.entry1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry1.place(
            x=232, y=342,
            width=260,
            height=38)

        self.entry2 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry2.place(
            x=232, y=282,
            width=260,
            height=38)

        self.entry3 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            state='disabled',
            font=("Inter-Regular", int(16.0)))

        self.entry3.place(
            x=232, y=166,
            width=260,
            height=38)

        self.entry4 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(16.0)))

        self.entry4.place(
            x=232, y=222,
            width=260,
            height=38)

        img2 = tk.PhotoImage(file=dirGUI + "btnAdd.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnAdd,
            relief="flat")

        b2.place(
            x=42, y=565,
            width=120,
            height=50)

        img3 = tk.PhotoImage(file=dirGUI + "btnDelete.png")
        b3 = tk.Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnDelete,
            relief="flat")

        b3.place(
            x=330, y=565,
            width=120,
            height=50)

        img4 = tk.PhotoImage(file=dirGUI + "btnEdit.png")
        b4 = tk.Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnEdit,
            relief="flat")

        b4.place(
            x=186, y=565,
            width=120,
            height=50)

        options = ["ID", "Name", "Phone", "Email"]
        self.clicked = tk.StringVar()
        self.clicked.set(options[0])

        entry5 = tk.OptionMenu(self, self.clicked, *options)

        entry5.place(
            x=805, y=116,
            width=153,
            height=35)

        self.entry6 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            highlightthickness=0,
            font=("Inter-Regular", int(12.0)))

        self.entry6.place(
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

        img6 = tk.PhotoImage(file=dirGUI + "btnRevert.png")
        b6 = tk.Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.loadLecturer,
            relief="flat")

        b6.place(
            x=1204, y=116,
            width=56,
            height=39)

        columns = ('ID', 'Name', 'Phone', 'Email')

        self.b7 = ttk.Treeview(self, columns=columns, show='headings')
        self.b7.heading('ID', text='ID')
        self.b7.column('ID', width=50, anchor=tk.CENTER)
        self.b7.heading('Name', text='Name')
        self.b7.column('Name', width=150, anchor=tk.W)
        self.b7.heading('Phone', text='Phone')
        self.b7.column('Phone', width=80, anchor=tk.W)
        self.b7.heading('Email', text='Email')
        self.b7.column('Email', width=150, anchor=tk.W)

        self.b7.bind('<<TreeviewSelect>>', self.itemSelect)

        self.b7.place(
            x=660, y=166,
            width=596,
            height=530)

        self.role = getSession()[-1]
        self.userID = getUser()[0]
        self.tick = None
        self.loadLecturer()
        self.clock()
        self.title('VKU Attendance')
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m6.Menu()

    def btnAdd(self):
        if self.role == 'A':
            if self.entry3.get() == '':
                name = self.entry4.get()
                phone = self.entry2.get()
                email = self.entry1.get()
                password = self.entry0.get()
                if all(v != '' for v in [name, phone, email, password]):
                    addLecturer(name, phone, email, password)
                    self.btnReset()
                    self.loadLecturer()
                    messagebox.showinfo('Success', 'Add lecturer success!')
                else:
                    messagebox.showinfo('Empty entry', 'Please fill all entries!')
            else:
                messagebox.showinfo('Reset ID', 'Please click Reset button first!')
        else:
            messagebox.showinfo('Insufficient permissions', 'This function is for admin only!')

    def btnEdit(self):
        id = self.entry3.get()
        if id != '':
            name = self.entry4.get()
            phone = self.entry2.get()
            email = self.entry1.get()
            password = self.entry0.get()
            if all(v != '' for v in [name, phone, email, password]):
                if self.role != 'L' and self.userID != id:
                    messagebox.showinfo('Insufficient permissions', 'Can not edit other lecturer information!')
                else:
                    oldPass = simpledialog.askstring('Password confirm', 'Please re-enter old password:')
                    if oldPass == getUser()[2]:
                        editLecturer(id, name, phone, email, password)
                        self.btnReset()
                        self.loadLecturer()
                        messagebox.showinfo('Success', 'Edit Lecturer success!')
                    else:
                        messagebox.showinfo('Failed', 'Incorrect old password!')
            else:
                messagebox.showinfo('Empty entry', 'Please fill all entries!')
        else:
            messagebox.showinfo('Not have ID', 'Please select lecturer in list first!')

    def btnDelete(self):
        if self.role == 'A':
            id = self.entry3.get()
            if id != '':
                ask = messagebox.askquestion('Delete lecturer', 'Are you sure to delete this lecturer?', icon='warning')
                if ask == 'yes':
                    deleteLecturer(id)
                    self.btnReset()
                    self.loadLecturer()
                    messagebox.showinfo('Success', "Delete lecturer success!")
            else:
                messagebox.showinfo('Not have ID', 'Please select lecturer in list first!')
        else:
            messagebox.showinfo('Insufficient permissions', 'This function is for admin only!')

    def btnReset(self):
        self.entry0.configure(show='')
        setEntry(self.entry0, '')
        setEntry(self.entry1, '')
        setEntry(self.entry2, '')
        self.entry3.configure(state='normal')
        setEntry(self.entry3, '')
        self.entry3.configure(state='disabled')
        setEntry(self.entry4, '')

    def btnSearch(self):
        value = self.entry6.get()
        if value != '':
            col = self.clicked.get()
            if col == "ID":
                col = "id"
            elif col == "Name":
                col = "name"
            elif col == "Phone":
                col = "phone"
            else:
                col = "email"
            for item in self.b7.get_children():
                self.b7.delete(item)
            list = searchLecturer(col, value)
            for x in list:
                self.b7.insert('', tk.END, values=x)
        else:
            messagebox.showinfo("Empty entry", "Please fill in entry!")

    def loadLecturer(self):
        for item in self.b7.get_children():
            self.b7.delete(item)
        list = listLecturer()
        for x in list:
            self.b7.insert('', tk.END, values=x)

    def clock(self):
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def itemSelect(self, _):
        for s in self.b7.selection():
            item = self.b7.item(s)
            lecturer = item['values']
            self.entry3.configure(state='normal')
            setEntry(self.entry3, lecturer[0])
            self.entry3.configure(state='disabled')
            setEntry(self.entry4, lecturer[1])
            setEntry(self.entry2, lecturer[2])
            setEntry(self.entry1, lecturer[3])
            if self.role == 'L' and self.userID != lecturer[0]:
                self.entry0.configure(show='*')
            else:
                self.entry0.configure(show='')
            setEntry(self.entry0, lecturer[4])
