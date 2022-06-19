import tkinter as tk
import os
from tkinter import messagebox
from ConnectDatabase import isAdmin, createAdmin, isLecturer, createLecturer
from Menu import Menu

dirGUI = os.getcwd() + "\\gui\\"


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720+100+50")
        self.configure(bg="#ffffff")
        canvas = tk.Canvas(
            self,
            bg="#ffffff",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        icon = tk.PhotoImage(file=dirGUI + 'icon.png')
        self.iconphoto(False, icon)

        background_img = tk.PhotoImage(file=dirGUI + "bgLogin.png")
        canvas.create_image(
            774.5, 461.5,
            image=background_img)

        entry0_img = tk.PhotoImage(file=dirGUI + "textLogin.png")
        canvas.create_image(
            896.0, 397.0,
            image=entry0_img)

        self.entry0 = tk.Entry(
            show='*',
            font='Inter 18',
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        self.entry0.place(
            x=697.0, y=368,
            width=398.0,
            height=56)

        entry1_img = tk.PhotoImage(file=dirGUI + "textLogin.png")
        canvas.create_image(
            896.0, 290.0,
            image=entry1_img)

        self.entry1 = tk.Entry(
            font='Inter 18',
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        self.entry1.place(
            x=697.0, y=261,
            width=398.0,
            height=56)

        img0 = tk.PhotoImage(file=dirGUI + "btnLogin.png")
        b0 = tk.Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnLogin,
            relief="flat")

        b0.place(
            x=841, y=460,
            width=110,
            height=47)

        self.title('VKU Attendance')
        self.resizable(False, False)
        self.mainloop()

    def btnLogin(self):
        t0 = self.entry1.get()
        t1 = self.entry0.get()
        if isAdmin(t0, t1):
            createAdmin(t0, t1)
            self.destroy()
            Menu()
        elif isLecturer(t0, t1):
            createLecturer(t0, t1)
            self.destroy()
            Menu()
        else:
            messagebox.showinfo('Login Failed', 'Wrong email or password!')
