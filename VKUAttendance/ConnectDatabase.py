import mysql.connector
import Session as s
import os

mydb = mysql.connector.connect(host="localhost", user="Quang Sang", passwd="392001", database="vkuattendance")
dirDataset = os.getcwd() + "\\dataset\\"


def isAdmin(username, password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM admin")
    result = mycursor.fetchall()
    for x in result:
        if x[1] == username and x[2] == password:
            return True
    return False


def createAdmin(username, password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM admin WHERE username='" + username + "' AND pass='" + password + "'")
    result = mycursor.fetchone()
    s.createSession(str(result[0]) + "A")


def isLecturer(email, password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM lecturer")
    result = mycursor.fetchall()
    for x in result:
        if x[3] == email and x[4] == password:
            return True
    return False


def createLecturer(email, password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM lecturer WHERE email='" + email + "' AND pass='" + password + "'")
    result = mycursor.fetchone()
    s.createSession(str(result[0]) + "L")


def getUser():
    session = s.getSession()
    if session[-1] == 'A':
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM admin WHERE id='" + session[0] + "'")
        result = mycursor.fetchone()
        return result
    else:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM lecturer WHERE id='" + session[0] + "'")
        result = mycursor.fetchone()
        return result


def addStudent(name, classS, code, phone, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO student (name, class, code, phone, email) VALUES (%s, %s, %s, %s, %s)"
    val = (name, classS, code, phone, email)
    mycursor.execute(sql, val)
    mydb.commit()


def editStudent(id, name, classS, code, phone, email):
    mycursor = mydb.cursor()
    sql = "UPDATE student SET name=%s, class=%s, code=%s, phone=%s, email=%s WHERE id =%s"
    val = (name, classS, code, phone, email, id)
    mycursor.execute(sql, val)
    mydb.commit()


def deleteStudent(id):
    deleteImage(id)
    mycursor1 = mydb.cursor()
    sql1 = "DELETE FROM attendance WHERE idStudent='" + str(id) + "'"
    mycursor1.execute(sql1)
    mydb.commit()
    mycursor2 = mydb.cursor()
    sql2 = "DELETE FROM course WHERE idStudent='" + str(id) + "'"
    mycursor2.execute(sql2)
    mydb.commit()
    mycursor = mydb.cursor()
    sql = "DELETE FROM student WHERE id='" + id + "'"
    mycursor.execute(sql)
    mydb.commit()


def checkImage(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM image WHERE idStudent='" + str(id) + "'")
    result = mycursor.fetchall()
    if result:
        return True
    else:
        return False


def deleteImage(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM image WHERE idStudent='" + str(id) + "'"
    mycursor.execute(sql)
    mydb.commit()


def saveImageStudent(id):
    mycursor = mydb.cursor()
    for i in range(1, 31):
        with open(dirDataset + str(id) + '-' + str(i) + ".png", "rb") as File:
            binaryData = File.read()
        sql = "INSERT INTO image (idStudent, name, data) VALUES (%s, %s, %s)"
        name = str(id) + '-' + str(i) + ".png"
        val = (id, name, binaryData)
        mycursor.execute(sql, val)
        mydb.commit()


def searchStudent(col, value):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM student WHERE " + col + " LIKE '%" + value + "%'")
    result = mycursor.fetchall()
    return result


def listStudent():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM student")
    result = mycursor.fetchall()
    return result


def addLecturer(name, phone, email, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO lecturer (name, phone, email, pass) VALUES (%s, %s, %s, %s)"
    val = (name, phone, email, password)
    mycursor.execute(sql, val)
    mydb.commit()


def editLecturer(id, name, phone, email, password):
    mycursor = mydb.cursor()
    sql = "UPDATE lecturer SET name=%s, phone=%s, email=%s, pass=%s WHERE id =%s"
    val = (name, phone, email, password, id)
    mycursor.execute(sql, val)
    mydb.commit()


def deleteLecturer(id):
    lesson = listLessonLecturer(id)
    for i in lesson:
        mycursor1 = mydb.cursor()
        sql1 = "DELETE FROM attendance WHERE idLesson='" + str(i[0]) + "'"
        mycursor1.execute(sql1)
        mydb.commit()
    mycursor2 = mydb.cursor()
    sql2 = "DELETE FROM lesson WHERE idLecturer='" + str(id) + "'"
    mycursor2.execute(sql2)
    mydb.commit()
    mycursor3 = mydb.cursor()
    sql3 = "DELETE FROM teach WHERE idLecturer='" + str(id) + "'"
    mycursor3.execute(sql3)
    mydb.commit()
    mycursor = mydb.cursor()
    sql = "DELETE FROM lecturer WHERE id='" + id + "'"
    mycursor.execute(sql)
    mydb.commit()


def listLecturer():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM lecturer")
    result = mycursor.fetchall()
    return result


def searchLecturer(col, value):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM lecturer WHERE " + col + " LIKE '%" + value + "%'")
    result = mycursor.fetchall()
    return result


def addSubject(name):
    mycursor = mydb.cursor()
    sql = "INSERT INTO subject ( name ) VALUES (%s)"
    val = (name,)
    mycursor.execute(sql, val)
    mydb.commit()


def lectureSubject(idSubject, idLecturer):
    mycursor = mydb.cursor()
    sql = "INSERT INTO teach (idSubject, idLecturer) VALUES (%s, %s)"
    val = (idSubject, idLecturer)
    mycursor.execute(sql, val)
    mydb.commit()


def renameSubject(id, name):
    mycursor1 = mydb.cursor()
    sql1 = "SELECT * FROM subject WHERE id ='" + id + "'"
    mycursor1.execute(sql1)
    nameO = mycursor1.fetchone()[1]
    if nameO == name:
        return False
    else:
        mycursor = mydb.cursor()
        sql = "UPDATE subject SET name=%s WHERE id =%s"
        val = (name, id)
        mycursor.execute(sql, val)
        mydb.commit()
        return True


def quitSubject(idSubject, idLecturer):
    mycursor1 = mydb.cursor()
    sql1 = "SELECT * FROM teach WHERE idSubject ='" + str(idSubject) + "' AND idLecturer='" + str(idLecturer) + "'"
    mycursor1.execute(sql1)
    ck = mycursor1.fetchone()
    if ck is None:
        return False
    else:
        mycursor = mydb.cursor()
        sql = "DELETE FROM teach WHERE idSubject='" + str(idSubject) + "' AND idLecturer='" + str(idLecturer) + "'"
        mycursor.execute(sql)
        mydb.commit()
        return True


def deleteSubject(id):
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT * FROM lesson WHERE idSubject='" + str(id) + "'")
    lesson = mycursor1.fetchall()
    for i in lesson:
        mycursor2 = mydb.cursor()
        sql2 = "DELETE FROM attendance WHERE idLesson='" + str(i[0]) + "'"
        mycursor2.execute(sql2)
        mydb.commit()
    mycursor3 = mydb.cursor()
    sql3 = "DELETE FROM teach WHERE idSubject='" + str(id) + "'"
    mycursor3.execute(sql3)
    mydb.commit()
    mycursor4 = mydb.cursor()
    sql4 = "DELETE FROM course WHERE idSubject='" + str(id) + "'"
    mycursor4.execute(sql4)
    mydb.commit()
    mycursor = mydb.cursor()
    sql = "DELETE FROM subject WHERE id='" + id + "'"
    mycursor.execute(sql)
    mydb.commit()


def listSubject():
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT * FROM subject")
    result1 = mycursor1.fetchall()
    list = []
    for i in result1:
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT COUNT(idSubject) AS 'Total' FROM teach WHERE idSubject='" + str(i[0]) + "'")
        result2 = mycursor2.fetchone()
        list.append((i[0], i[1], result2[0]))
    return tuple(list)


def searchSubject(col, value):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM subject WHERE " + col + " LIKE '%" + value + "%'")
    result = mycursor.fetchall()
    list = []
    for i in result:
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT COUNT(idSubject) AS 'Total' FROM teach WHERE idSubject='" + str(i[0]) + "'")
        result2 = mycursor2.fetchone()
        list.append((i[0], i[1], result2[0]))
    return tuple(list)


def listLecturerSubject(id):
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT id, name FROM lecturer")
    result1 = mycursor1.fetchall()
    list = []
    for i in result1:
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT * FROM teach WHERE idLecturer='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
        result2 = mycursor2.fetchone()
        if result2 is not None:
            list.append((i[0], i[1], 'Yes'))
        else:
            list.append((i[0], i[1], 'No'))
    return tuple(list)


def searchLectureSubject(col, value, id):
    if col == 'id' or col == 'name':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT id, name FROM lecturer WHERE " + col + " LIKE '%" + value + "%'")
        result1 = mycursor1.fetchall()
        list = []
        for i in result1:
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "SELECT * FROM teach WHERE idLecturer='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
            result2 = mycursor2.fetchone()
            if result2 is not None:
                list.append((i[0], i[1], 'Yes'))
            else:
                list.append((i[0], i[1], 'No'))
        return tuple(list)
    elif col == 'Lecture' and value == 'Yes' or value == 'yes' or value == 'y':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT id, name FROM lecturer")
        result1 = mycursor1.fetchall()
        list = []
        for i in result1:
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "SELECT * FROM teach WHERE idLecturer='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
            result2 = mycursor2.fetchone()
            if result2 is not None:
                list.append((i[0], i[1], 'Yes'))
        return tuple(list)
    elif col == 'Lecture' and value == 'No' or value == 'no' or value == 'n':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT id, name FROM lecturer")
        result1 = mycursor1.fetchall()
        list = []
        for i in result1:
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "SELECT * FROM teach WHERE idLecturer='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
            result2 = mycursor2.fetchone()
            if result2 is None:
                list.append((i[0], i[1], 'No'))
        return tuple(list)


def learnSubject(idSubject, idStudent):
    mycursor = mydb.cursor()
    sql = "INSERT INTO course (idSubject, idStudent) VALUES (%s, %s)"
    val = (idSubject, idStudent)
    mycursor.execute(sql, val)
    mydb.commit()


def expelSubject(idSubject, idStudent):
    mycursor1 = mydb.cursor()
    sql1 = "DELETE FROM attendance WHERE idStudent='" + str(idStudent) + "'"
    mycursor1.execute(sql1)
    mydb.commit()
    mycursor = mydb.cursor()
    sql = "DELETE FROM course WHERE idSubject='" + str(idSubject) + "' AND idStudent='" + str(idStudent) + "'"
    mycursor.execute(sql)
    mydb.commit()


def listStudentSubject(id):
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT id, name FROM student")
    result1 = mycursor1.fetchall()
    list = []
    for i in result1:
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT * FROM course WHERE idStudent='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
        result2 = mycursor2.fetchone()
        if result2 is not None:
            list.append((i[0], i[1], 'Yes'))
        else:
            list.append((i[0], i[1], 'No'))
    return tuple(list)


def listStudentScan(id, idLesson):
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT id, name FROM student")
    result1 = mycursor1.fetchall()
    list = []
    for i in result1:
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT * FROM course WHERE idStudent='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
        result2 = mycursor2.fetchone()
        if result2 is not None:
            mycursor3 = mydb.cursor()
            mycursor3.execute(
                "SELECT * FROM attendance WHERE idStudent='" + str(i[0]) + "' AND idLesson='" + str(idLesson) + "'")
            result3 = mycursor3.fetchone()
            if result3 is not None:
                list.append((i[0], i[1], 'Yes'))
            else:
                list.append((i[0], i[1], 'No'))
    return tuple(list)


def searchStudentSubject(col, value, id):
    if col == 'id' or col == 'name':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT id, name FROM student WHERE " + col + " LIKE '%" + value + "%'")
        result1 = mycursor1.fetchall()
        list = []
        for i in result1:
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "SELECT * FROM course WHERE idStudent='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
            result2 = mycursor2.fetchone()
            if result2 is not None:
                list.append((i[0], i[1], 'Yes'))
            else:
                list.append((i[0], i[1], 'No'))
        return tuple(list)
    elif col == 'Learn' and value == 'Yes' or value == 'yes' or value == 'y':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT id, name FROM student")
        result1 = mycursor1.fetchall()
        list = []
        for i in result1:
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "SELECT * FROM course WHERE idStudent='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
            result2 = mycursor2.fetchone()
            if result2 is not None:
                list.append((i[0], i[1], 'Yes'))
        return tuple(list)
    elif col == 'Learn' and value == 'No' or value == 'no' or value == 'n':
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT id, name FROM student")
        result1 = mycursor1.fetchall()
        list = []
        for i in result1:
            mycursor2 = mydb.cursor()
            mycursor2.execute(
                "SELECT * FROM course WHERE idStudent='" + str(i[0]) + "' AND idSubject='" + str(id) + "'")
            result2 = mycursor2.fetchone()
            if result2 is None:
                list.append((i[0], i[1], 'No'))
        return tuple(list)


def addLesson(subject, idLecturer, timeStart, timeEnd):
    date = s.getDateSQL()
    mycursorId = mydb.cursor()
    mycursorId.execute("SELECT * FROM subject WHERE name='" + subject + "'")
    resultId = mycursorId.fetchone()
    idSubject = resultId[0]
    mycursor = mydb.cursor()
    sql = "INSERT INTO lesson (idSubject, idLecturer, date, timeStart, timeEnd ) VALUES (%s, %s, %s, %s, %s)"
    val = (idSubject, idLecturer, date, timeStart, timeEnd)
    mycursor.execute(sql, val)
    mydb.commit()


def editLesson(id, timeStart, timeEnd):
    mycursor = mydb.cursor()
    sql = "UPDATE lesson SET timeStart=%s, timeEnd=%s WHERE id =%s"
    val = (timeStart, timeEnd, id)
    mycursor.execute(sql, val)
    mydb.commit()


def deleteLesson(id):
    mycursor1 = mydb.cursor()
    sql1 = "DELETE FROM attendance WHERE idLesson='" + str(id) + "'"
    mycursor1.execute(sql1)
    mydb.commit()
    mycursor = mydb.cursor()
    sql = "DELETE FROM lesson WHERE id='" + id + "'"
    mycursor.execute(sql)
    mydb.commit()


def searchLesson(col, value):
    if col != 'You':
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT lesson.id, subject.name, date, timeStart, timeEnd, lecturer.name, lecturer.id FROM lesson INNER "
            "JOIN subject ON lesson.idSubject = subject.id INNER JOIN lecturer ON lesson.idLecturer = lecturer.id "
            "WHERE " + col + " LIKE '%" + value + "%' ORDER BY lesson.id")
        result = mycursor.fetchall()
    else:
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT lesson.id, subject.name, date, timeStart, timeEnd, lecturer.name, lecturer.id FROM lesson INNER "
            "JOIN subject ON lesson.idSubject = subject.id INNER JOIN lecturer ON lesson.idLecturer = lecturer.id "
            "WHERE lecturer.id='" + value + "' ORDER BY lesson.id")
        result = mycursor.fetchall()
    list = []
    for i in result:
        list.append((i[0], i[1], s.dateFormat(str(i[2])), i[3], i[4], i[5], i[6]))
    return tuple(list)


def listLesson():
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT lesson.id, subject.name, date, timeStart, timeEnd, lecturer.name, lecturer.id FROM lesson INNER JOIN "
        "subject ON lesson.idSubject = subject.id INNER JOIN lecturer ON lesson.idLecturer = lecturer.id ORDER BY "
        "lesson.id")
    result = mycursor.fetchall()
    list = []
    for i in result:
        list.append((i[0], i[1], s.dateFormat(str(i[2])), i[3], i[4], i[5], i[6]))
    return tuple(list)


def listSubjectOptions(id):
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT id, name FROM subject")
    result1 = mycursor1.fetchall()
    list = []
    for i in result1:
        mycursor2 = mydb.cursor()
        mycursor2.execute("SELECT * FROM teach WHERE idSubject='" + str(i[0]) + "' AND idLecturer='" + str(id) + "'")
        result2 = mycursor2.fetchone()
        if result2 is not None:
            list.append(i[1])
    return tuple(list)


def listLessonLecturer(id):
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT lesson.id, subject.name, date, timeStart, timeEnd, lesson.idSubject FROM lesson INNER JOIN subject ON "
        "lesson.idSubject = subject.id WHERE lesson.idLecturer='" + str(id) + "'  ORDER BY lesson.id")
    result = mycursor.fetchall()
    list = []
    for i in result:
        if s.checkLessonEnd(i[2], i[4]):
            list.append(i)
    return tuple(list)


def getImageStudent(id):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM image WHERE idStudent='" + str(id) + "'")
    result = mycursor.fetchall()
    for image in result:
        path = dirDataset + image[2]
        with open(path, "wb") as File:
            File.write(image[3])
            File.close()


def attendStudent(idStudent, idLesson, timeAttend, typeAttend):
    idStudent = str(idStudent)
    idLesson = str(idLesson)
    date = s.dateFormat(timeAttend.split(' ')[0]) + ' ' + timeAttend.split(' ')[1]
    mycursor = mydb.cursor()
    sql = "INSERT INTO attendance (idStudent, idLesson, time, type ) VALUES (%s, %s, %s, %s)"
    val = (idStudent, idLesson, date, typeAttend)
    mycursor.execute(sql, val)
    mydb.commit()


def isAttend(idStudent, idLesson, typeAttend):
    idStudent = str(idStudent)
    idLesson = str(idLesson)
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM attendance WHERE idStudent='" + idStudent + "' AND idLesson='" +
        idLesson + "' AND type='" + typeAttend + "'")
    result = mycursor.fetchone()
    if result:
        return "Yes"
    else:
        return "No"


def isLessonLecturer(idLesson, idLecturer):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM lesson WHERE id='" + idLesson + "'")
    result = mycursor.fetchone()
    if idLecturer == result[2]:
        return True
    else:
        return False


def fixAttendance(id):
    mycursor = mydb.cursor()
    sql = "UPDATE attendance SET type=%s WHERE id =%s"
    val = ('Present(X)', id)
    mycursor.execute(sql, val)
    mydb.commit()


def deleteAttendance(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM attendance WHERE id='" + id + "'"
    mycursor.execute(sql)
    mydb.commit()


def listAttendance():
    list = []
    mycursor = mydb.cursor()
    mycursor.execute("SELECT attendance.id, attendance.idStudent, student.name, attendance.type, attendance.idLesson, "
                     "attendance.time FROM attendance JOIN student ON attendance.idStudent=student.id ORDER BY "
                     "attendance.id")
    result = mycursor.fetchall()
    for i in result:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT subject.name, lesson.timeStart, lesson.timeEnd, lesson.date FROM lesson JOIN subject "
                         "ON lesson.idSubject=subject.id WHERE lesson.id='" + str(i[4]) + "'")
        result1 = mycursor.fetchone()
        if i[3] == "Absent" or i[3] == "Present(X)":
            list.append((i[0], i[1], i[2], result1[0], str(result1[1]) + '-' + str(result1[2]),
                         s.dateFormat(str(result1[3])), i[3], i[4]))
        else:
            list.append((i[0], i[1], i[2], result1[0], str(result1[1]) + '-' + str(result1[2]),
                         s.dateFormat(str(result1[3])), s.checkAttendStatus(i[5], result1[1]) + "(" + i[3] + ")", i[4]))
    return tuple(list)


def searchAttendance(col, val):
    list = listAttendance()
    result = []
    if col == "ID":
        ck = 0
    elif col == "ID Student":
        ck = 1
    elif col == "Student":
        ck = 2
    elif col == "Subject":
        ck = 3
    elif col == "Time":
        ck = 4
    elif col == "Date":
        ck = 5
    elif col == "Attend":
        ck = 6
    else:
        ck = 7
    for i in list:
        if val in str(i[ck]):
            result.append(i)
    return tuple(result)


def listStatistic():
    list = []
    mycursor = mydb.cursor()
    mycursor.execute("SELECT attendance.idStudent, student.name, attendance.type, attendance.idLesson, "
                     "attendance.time FROM attendance JOIN student ON attendance.idStudent=student.id")
    result = mycursor.fetchall()
    for i in result:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT subject.name, lesson.timeStart, lesson.date FROM lesson JOIN subject "
                         "ON lesson.idSubject=subject.id WHERE lesson.id='" + str(i[3]) + "'")
        result1 = mycursor.fetchone()
        if i[2] == "Absent" or i[2] == "Present(X)":
            list.append((i[0], i[1], s.dateFormat(str(result1[2])), result1[0], i[3], i[2]))
        else:
            list.append((i[0], i[1], s.dateFormat(str(result1[2])), result1[0], i[3],
                         s.checkAttendStatus(i[4], result1[1]) + "(" + i[2] + ")"))
    return tuple(list)


def searchStatistic(col, status, value):
    list = listStatistic()
    result = []
    if col == "ID":
        ck = 0
    elif col == "Name":
        ck = 1
    elif col == "Date":
        ck = 2
    elif col == "Subject":
        ck = 3
    elif col == "ID Lesson":
        ck = 4
    else:
        ck = 5
    for i in list:
        if value in str(i[ck]):
            result.append(i)
    return searchStatus(result, status)


def searchStatus(list, status):
    if status == 'All':
        return list
    present = []
    presentX = []
    late = []
    absent = []
    for i in list:
        if 'Present(X)' == i[5]:
            presentX.append(i)
        elif 'Late' in i[5]:
            late.append(i)
        elif 'Absent' in i[5]:
            absent.append(i)
        else:
            present.append(i)
    if status == 'Present':
        return tuple(present)
    elif status == 'Late':
        return tuple(late)
    elif status == 'Absent':
        return tuple(absent)
    elif status == 'Present(X)':
        return tuple(presentX)
    elif status == 'Present-Present(X)':
        return tuple(present + presentX)
    elif status == 'Late-Absent':
        return tuple(late + absent)
    else:
        return list
