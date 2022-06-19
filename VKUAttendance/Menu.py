import tkinter as tk
import os
import Login as l1

from tkinter import messagebox
from Student import Student
from Scan import Scan
from Attend import Attend
from Subject import Subject
from Statistic import Statistic
from Lecturer import Lecturer
from Lesson import Lesson
from ConnectDatabase import getUser
from Session import dateTime, getSession

dir = os.getcwd() + "\\"
dirGUI = os.getcwd() + "\\gui\\"
dirPicture = os.getcwd() + "\\images\\"


def btnPicture():
    os.startfile(dirPicture)


class Menu(tk.Tk):
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

        img0 = tk.PhotoImage(file=dirGUI + "btnStudent.png")
        b0 = tk.Button(
            image=img0,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnStudent,
            relief="flat")

        b0.place(
            x=202, y=155,
            width=200,
            height=200)

        img1 = tk.PhotoImage(file=dirGUI + "btnPicture.png")
        b1 = tk.Button(
            image=img1,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=btnPicture,
            relief="flat")

        b1.place(
            x=877, y=399,
            width=200,
            height=200)

        img2 = tk.PhotoImage(file=dirGUI + "btnLesson.png")
        b2 = tk.Button(
            image=img2,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLesson,
            relief="flat")

        b2.place(
            x=652, y=399,
            width=200,
            height=200)

        img3 = tk.PhotoImage(file=dirGUI + "btnLecturer.png")
        b3 = tk.Button(
            image=img3,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLecturer,
            relief="flat")

        b3.place(
            x=427, y=399,
            width=200,
            height=200)

        img4 = tk.PhotoImage(file=dirGUI + "btnStatistic.png")
        b4 = tk.Button(
            image=img4,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnStatistic,
            relief="flat")

        b4.place(
            x=202, y=399,
            width=200,
            height=200)

        img5 = tk.PhotoImage(file=dirGUI + "btnSubject.png")
        b5 = tk.Button(
            image=img5,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnSubject,
            relief="flat")

        b5.place(
            x=877, y=155,
            width=200,
            height=200)

        img6 = tk.PhotoImage(file=dirGUI + "btnAttend.png")
        b6 = tk.Button(
            image=img6,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnAttend,
            relief="flat")

        b6.place(
            x=652, y=155,
            width=200,
            height=200)

        img7 = tk.PhotoImage(file=dirGUI + "btnScan.png")
        b7 = tk.Button(
            image=img7,
            bg='white',
            borderwidth=0,
            highlightthickness=0,
            command=self.btnScan,
            relief="flat")

        b7.place(
            x=427, y=155,
            width=200,
            height=200)

        background_img = tk.PhotoImage(file=dirGUI + "bgMenu.png")
        self.canvas.create_image(
            638.5, 385.5,
            image=background_img)

        self.b10 = self.canvas.create_text(
            1170.0, 48.0,
            text="99:99:99 PM\n20-04-2021",
            fill="#000000",
            font=("Inter-Regular", int(24.0)))

        img8 = tk.PhotoImage(file=dirGUI + "btnLogout.png")
        b8 = tk.Button(
            image=img8,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLogout,
            relief="flat")

        b8.place(
            x=14, y=13,
            width=65,
            height=65)

        b9 = tk.Label(text="User: " + getUser()[1],
                      anchor='w',
                      bg='white',
                      borderwidth=0,
                      highlightthickness=0,
                      relief="flat",
                      font=("Inter-Regular", int(24.0)))
        b9.place(x=10, y=675, width=500, height=32)

        self.role = getSession()[-1]
        self.tick = None
        self.clock()
        self.title('VKU Attendance')
        self.resizable(False, False)
        self.mainloop()

    def btnLogout(self):
        self.canvas.after_cancel(self.tick)
        os.remove(dir + 'session.txt')
        self.destroy()
        l1.Login()

    def btnStudent(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        Student()

    def btnScan(self):
        if self.role == 'L':
            self.canvas.after_cancel(self.tick)
            self.destroy()
            Scan()
        else:
            messagebox.showinfo('Insufficient permissions', 'This feature is for lecturer only!')

    def btnAttend(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        Attend()

    def btnSubject(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        Subject()

    def btnStatistic(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        Statistic()

    def btnLecturer(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        Lecturer()

    def btnLesson(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        Lesson()

    def clock(self):
        self.canvas.itemconfig(self.b10, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)
