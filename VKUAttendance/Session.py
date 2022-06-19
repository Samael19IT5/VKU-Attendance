import os
import time
from datetime import datetime

dir = os.getcwd()


def createSession(info):
    f = open(dir + '\\session.txt', 'w')
    f.truncate(0)
    f.write(info)
    f.close()


def getSession():
    f = open(dir + '\\session.txt', 'r')
    return f.readline()


def dateTime():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")
    am_pm = time.strftime("%p")
    return hour + ":" + minute + ":" + second + " " + am_pm + "\n" + day + "-" + month + "-" + year


def dateAttend():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")
    return day + "-" + month + "-" + year + ' ' + hour + ":" + minute + ":" + second


def getDateSQL():
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    return year + month + day


def dateFormat(d):
    array = d.split('-')
    return array[2] + '-' + array[1] + '-' + array[0]


def checkTime(start, end):
    fStart = start.split(':')
    fStart = list(map(int, fStart))
    fEnd = end.split(':')
    fEnd = list(map(int, fEnd))
    if fEnd[0] > 24 or fStart[1] > 24:
        return False
    else:
        if fEnd[1] > 60 or fStart[1] > 60:
            return False
        else:
            return True


def compareTime(start, end):
    fStart = start.split(':')
    fStart = list(map(int, fStart))
    fEnd = end.split(':')
    fEnd = list(map(int, fEnd))
    if fEnd[0] < fStart[0]:
        return False
    else:
        tmp = fEnd[0] - fStart[0]
        if (fEnd[1] + tmp * 60) - fStart[1] < 45:
            return False
        else:
            return True


def checkLessonEnd(currentDay, timeEnd):
    dateNow = str(datetime.now()).split(' ')[0]
    dateNowObj = datetime.strptime(dateNow, '%Y-%m-%d')
    if currentDay == datetime.date(dateNowObj):
        timeNow = str(datetime.now()).split(' ')[1]
        timeNow = timeNow.split('.')[0]
        timeNowObj = datetime.strptime(timeNow, '%H:%M:%S')
        timeEndObj = datetime.strptime(str(timeEnd), '%H:%M:%S')
        if timeEndObj > timeNowObj:
            return True
        else:
            return False
    else:
        return False


def checkLessonOver(timeEnd):
    timeNow = str(datetime.now()).split(' ')[1]
    timeNow = timeNow.split('.')[0]
    timeNowObj = datetime.strptime(timeNow, '%H:%M:%S')
    timeEndObj = datetime.strptime(str(timeEnd), '%H:%M:%S')
    if timeEndObj > timeNowObj:
        return False
    else:
        return True


def checkAttendStatus(datetimeS, timeStart):
    timeS = str(datetimeS).split(' ')[1]
    timeSObj = datetime.strptime(timeS, '%H:%M:%S')
    timeStartObj = datetime.strptime(str(timeStart), '%H:%M:%S')
    if timeSObj < timeStartObj:
        return "Present"
    else:
        late = str(timeSObj - timeStartObj)
        return "Late "+late
