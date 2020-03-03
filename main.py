import names
import csv
from datasheet import Datasheet
from student import Student
from random import choice, randrange

def makeStudent():

    firstname = choice(names.firstnames)
    lastname = choice(names.lastnames)
    gender = ("male" if (randrange(1,3) / 2) == 1 else "female")
    courses = []

    for i in range(0, randrange(1,4)):
        courses.append(names.courselist[i])

    ds = Datasheet(courses)

    return Student(firstname + " " + lastname, gender, ds)

def makeStudents(num):

    listStudents = []

    for i in range(0, num):
        listStudents.append(makeStudent())
    return listStudents

studs = makeStudents(3)

def writeToCSV():
    with open('students.csv', 'w', newline='') as csvfile:
        fieldnames = ['NAME', 'GENDER', 'DATASHEET']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in studs:
            writer.writerow({'NAME': student.name, 'GENDER': student.gender, 'DATASHEET': student.datasheet})

def readCSV():
    with open('students.csv', newline='') as studentfile:
        reader = csv.reader(studentfile)
        retLst = list(reader)
       
    return retLst

writeToCSV()

lst = readCSV()

for l in lst:
    print(l)
    for i in l:
        print(i)
