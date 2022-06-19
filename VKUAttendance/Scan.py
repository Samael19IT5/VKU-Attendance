import tkinter as tk
import os
import cv2
import numpy as np
import Menu as m2
import unidecode
from PIL import Image as Img, ImageTk
from tkinter import messagebox
from ConnectDatabase import getUser, listLessonLecturer, listStudentScan, getImageStudent, attendStudent, isAttend
from Session import dateTime, getSession, dateAttend, checkLessonOver

dir = os.getcwd()
dirGUI = os.getcwd() + "\\gui\\"
dirCascade = os.getcwd() + "\\cascade\\"
dirDataset = os.getcwd() + "\\dataset\\"
dirTrainer = os.getcwd() + "\\trainer\\"
dirImages = os.getcwd() + "\\images\\"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(dirCascade + "haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX
attendStudentList = []


def setEntry(entry: tk.Entry, text: str):
    entry.delete(0, tk.END)
    entry.insert(0, text)


def trainData():
    imagePaths = [os.path.join('dataset', f) for f in os.listdir('dataset')]
    faceSamples = []
    idS = []

    for imagePath in imagePaths:

        PIL_img = Img.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        id = int(os.path.split(imagePath)[-1].split("-")[0])
        faceS = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faceS:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            idS.append(id)

    recognizer.train(faceSamples, np.array(idS))
    recognizer.write(dirTrainer + "trainer.yml")


class Scan(tk.Tk):
    def __init__(self):
        super().__init__()
        self.role = getSession()[-1]
        self.userID = getUser()[0]
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

        background_img = tk.PhotoImage(file=dirGUI + "bgScan.png")
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

        img1 = tk.PhotoImage(file=dirGUI + "btnOpenM.png")
        b1 = tk.Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnOpen,
            relief="flat")

        b1.place(
            x=107, y=640,
            width=216,
            height=50)

        img2 = tk.PhotoImage(file=dirGUI + "btnCloseM.png")
        b2 = tk.Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btnClose,
            relief="flat")

        b2.place(
            x=389, y=640,
            width=216,
            height=50)

        self.entry0 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry0.place(
            x=980, y=655,
            width=200,
            height=34)

        self.entry1 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry1.place(
            x=980, y=605,
            width=200,
            height=34)

        self.entry2 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry2.place(
            x=980, y=555,
            width=200,
            height=34)

        self.entry3 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry3.place(
            x=980, y=460,
            width=200,
            height=34)

        self.entry4 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry4.place(
            x=980, y=360,
            width=200,
            height=34)

        self.entry5 = tk.Entry(
            bd=0,
            bg="#d9d9d9",
            font=("Inter-Regular", int(12.0)),
            highlightthickness=0)

        self.entry5.place(
            x=980, y=410,
            width=200,
            height=34)

        lessonOptions = []
        self.clickedLesson = tk.StringVar()
        self.clickedLesson.trace("w", self.lessonSelect)
        result = self.loadLesson()
        if result:
            for i in result:
                lessonOptions.append(str(i[1]).strip() + '#' + str(i[0]))
        else:
            lessonOptions.append('No lessons')
            self.clickedLesson.set(lessonOptions[0])

        self.entry6 = tk.OptionMenu(self, self.clickedLesson, *lessonOptions)

        self.entry6.place(
            x=129, y=108,
            width=330,
            height=37)

        typeOptions = ["In", "Out", "Sudden"]
        self.clickedType = tk.StringVar()

        self.entry7 = tk.OptionMenu(self, self.clickedType, *typeOptions)

        self.entry7.place(
            x=551, y=108,
            width=153,
            height=37)

        if self.clickedLesson.get() == "No lessons":
            self.entry6.configure(state='disabled')
            self.entry7.configure(state='disabled')

        self.imgCam = tk.PhotoImage(file=dirGUI + "imgCam.png")

        self.b3 = tk.Label(
            image=self.imgCam,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b3.place(
            x=25, y=155,
            width=679,
            height=475)

        self.imgStudent = tk.PhotoImage(file=dirGUI + "imgStudent.png")
        self.b4 = tk.Label(
            image=self.imgStudent,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b4.place(
            x=898, y=147,
            width=170,
            height=205)

        self.lessonID = None
        self.camTurned = False
        self.timeAttend = None
        self.expiry = None
        self.expiryCK = -1
        self.img = None
        self.attendStudentList = []
        self.cam = None
        self.subjectID = None
        self.tick = None
        self.clock()
        self.title("VKU Attendance")
        self.resizable(False, False)
        self.mainloop()

    def btnBack(self):
        self.canvas.after_cancel(self.tick)
        self.destroy()
        m2.Menu()

    def btnOpen(self):
        if self.entry2 != "" and self.clickedType.get() != "":
            if not checkLessonOver(self.expiry):
                self.expiryCK = 0
                listStudent = listStudentScan(self.subjectID, self.lessonID)
                self.attendStudentList = []
                for student in listStudent:
                    getImageStudent(student[0])
                    ck = isAttend(student[0], self.entry2.get(), self.clickedType.get())
                    self.attendStudentList.append([student[0], student[1], ck])
                trainData()
                recognizer.read(dirTrainer + "trainer.yml")
                self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                self.camTurned = True
                self.after(1, self.stream)
            else:
                messagebox.showinfo('Lesson is over', 'The end time of the lesson is: ' + str(self.expiry))
        else:
            messagebox.showinfo('Empty lesson or type', 'Please select lesson and type first!')

    def btnClose(self):
        self.camTurned = False
        self.resetStudent()

    def clock(self):
        if self.expiry is not None:
            if checkLessonOver(self.expiry) and self.expiryCK == 0:
                self.attendAbsent()
                self.expiryCK = 1
                self.btnClose()
                messagebox.showinfo('Lesson is over', 'The end time of the lesson is: ' + str(self.expiry))
        self.canvas.itemconfig(self.bTime, text=dateTime())
        self.tick = self.canvas.after(1000, self.clock)

    def resetStudent(self):
        self.imgStudent = tk.PhotoImage(file=dirGUI + "imgStudent.png")
        self.b4.configure(image=self.imgStudent)
        setEntry(self.entry3, '')
        setEntry(self.entry4, '')
        setEntry(self.entry5, '')

    def loadLesson(self):
        return listLessonLecturer(self.userID)

    def lessonSelect(self, *_):
        result = self.loadLesson()
        for i in result:
            if str(i[0]) == self.clickedLesson.get().split('#')[1]:
                setEntry(self.entry2, ' ' + str(i[0]))
                setEntry(self.entry1, ' ' + str(i[1]))
                setEntry(self.entry0, ' ' + str(i[3]) + ' - ' + str(i[4]))
                self.subjectID = i[5]
                self.lessonID = i[0]
                self.expiry = i[4]
                break

    def stream(self):
        _, self.img = self.cam.read()
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGBA)
        self.img = cv2.flip(self.img, 1)
        self.recognizerStudent()
        imgE = Img.fromarray(self.img)
        imgTk = ImageTk.PhotoImage(image=imgE)
        self.b3.imgTk = imgTk
        self.b3.configure(image=imgTk)
        if self.camTurned:
            self.b3.after(1, self.stream)
        else:
            self.cam.release()
            cv2.destroyAllWindows()
            self.b3.configure(image=self.imgCam)

    def recognizerStudent(self):
        minW = 0.1 * self.cam.get(3)
        minH = 0.1 * self.cam.get(4)
        ret, img = self.cam.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:

            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            idS, confidence = recognizer.predict(gray[y:y + h, x:x + w])


            if confidence <= 55:
                self.timeAttend = dateAttend()

                name = "Name: " + unidecode.unidecode(str(self.attendStudent(idS, gray[y:y + h, x:x + w])))
                idS = 'ID: ' + str(idS)
            else:
                idS = "unknown"
                name = ""

            cv2.putText(self.img, idS, (x + 5, y - 40), font, 0.8, (255, 162, 0), 2)
            cv2.putText(self.img, name, (x + 5, y - 10), font, 0.8, (255, 162, 0), 2)

    def attendStudent(self, id, imgArray):
        for i in self.attendStudentList:
            if str(i[0]) == str(id):
                if i[2] == "No":
                    attendStudent(i[0], self.entry2.get(), self.timeAttend, self.clickedType.get())
                    i[2] = "Yes"
                    setEntry(self.entry4, ' ' + str(i[0]))
                    setEntry(self.entry5, ' ' + str(i[1]))
                    setEntry(self.entry3, self.timeAttend)
                    cv2.imwrite(dirImages + str(i[0]) + " " + self.timeAttend.replace(':', '_') + ".png", imgArray)
                    self.imgStudent = tk.PhotoImage(
                        file=dirImages + str(i[0]) + " " + self.timeAttend.replace(':', '_') + ".png")
                    self.b4.configure(image=self.imgStudent)
                    self.timeAttend = None
                    if self.checkFull():
                        messagebox.showinfo('Attend completed', 'All students had attended!')
                return i[1]

    def attendAbsent(self):
        for i in self.attendStudentList:
            if i[2] == 'No':
                attendStudent(i[0], self.entry2.get(), self.timeAttend, "Absent")

    def checkFull(self):
        for i in self.attendStudentList:
            if i[2] == 'No':
                return False
        return True
