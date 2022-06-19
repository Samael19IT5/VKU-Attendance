import time
import tkinter as tk
import cv2
import os
from tkinter import messagebox
from PIL import Image as Img, ImageTk

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"
dirCascade = os.getcwd() + "\\cascade\\"
dirDataset = os.getcwd() + "\\dataset\\"
face_detector = cv2.CascadeClassifier(dirCascade + 'haarcascade_frontalface_default.xml')


class Image(tk.Toplevel):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.geometry("750x720+400+50")
        self.configure(bg="#ffffff")
        canvasCam = tk.Canvas(
            self,
            bg="#ffffff",
            height=720,
            width=750,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvasCam.place(x=0, y=0)

        icon = tk.PhotoImage(file=dirGUI + 'icon.png')
        self.iconphoto(False, icon)

        background_img = tk.PhotoImage(file=dirGUI + "bgStudentCam.png")
        canvasCam.create_image(
            377.5, 378.0,
            image=background_img)

        img0 = tk.PhotoImage(file=dirGUI + "btnCapture.png")
        self.b0 = tk.Button(
            self,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnCapture,
            relief="flat")

        self.b0.place(
            x=74, y=648,
            width=250,
            height=50)

        img1 = tk.PhotoImage(file=dirGUI + "btnClose.png")
        self.b1 = tk.Button(
            self,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnClose,
            relief="flat")

        self.b1.place(
            x=421, y=648,
            width=250,
            height=50)

        self.b2 = tk.Label(
            self,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b2.place(
            x=50, y=86,
            width=650,
            height=530)

        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.after(1, self.stream)
        self.resizable(False, False)
        self.mainloop()

    def btnCapture(self):
        count = 0
        while True:
            ret, img = self.cam.read()
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                count += 1

                cv2.imwrite(dirDataset + str(self.id) + '-' + str(count) + ".png", gray[y:y + h, x:x + w])

            if count >= 30:
                messagebox.showinfo('Captured', 'Capture completed!', parent=self)
                break
            else:
                time.sleep(0.2)

    def btnClose(self):
        self.cam.release()
        cv2.destroyAllWindows()
        self.destroy()

    def stream(self):
        _, frame = self.cam.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image = cv2.flip(cv2image, 1)
        img = Img.fromarray(cv2image)
        imgTk = ImageTk.PhotoImage(image=img)
        self.b2.imgTk = imgTk
        self.b2.configure(image=imgTk)
        self.b2.after(1, self.stream)
