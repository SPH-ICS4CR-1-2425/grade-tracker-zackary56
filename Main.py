#Grade Tracker
#zackaryizacc
# Grade: ICS4C
from pickletools import markobject
from random import choice


class SchoolClass:
    name = ""
    grades = []



    def __init__(self,name):
        self.name = name
        self.grades = []

    def addGrade(self,mark):
        self.grades.append(mark)

    def getAverge(self):
        return sum(self.grades)/len(self.grades)


#Main Menu function
def menu():
    want_Quit=False
    while not want_Quit:

        print("welcome")
        print("[1]pick a class")
        print("[2] addGrade")
        print("[3] review grade")
        print("[4] edit grades")
        print("[5] show average")
        print("[6] exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addClass()

        elif choice == 2:
            addGrade()
        elif choice == 3:
            reviewGrade()
        elif choice == 4:
            editGrades()
        elif choice == 5:
            showAverage()
        elif choice == 6:
             want_Quit = True


#Add a class function
def addClass():
    name = input("Enter your name of the class: ")
    classes.append(SchoolClass(name))


#Add a grade to a particular clss
def addGrade():
    #List the classes
    x=1
    for i in classes:
        print(x,i.name)
        x+=1

    choice=int(input("Enter your choice: "))-1
    mark = int(input("Enter your mark: "))
    classes[choice].addGrade(mark)

#Show the grades for a given class
def reviewGrade():
    x = 1
    for i in classes:
        print(x, i.name)
        x += 1
        print(i)
        choice=int(input("Enter your choice: "))-1
        x = 1
        for x in addGrade:
            print(x, classes.name)
            x += 1
    


    # List all the classes (look at addGrade)
    # user picks a class
    # list all the grades for that one class


#Edit the grades in a given class
def editGrades():
    x = 1
    for i in classes:
        print(x, i.name)
        x += 1
        choice = int(input("Enter your choice: ")) - 1
        print(mark)
        mark = int(input("Enter your mark: "))
        print(x)


#Show the average for a given class
def showAverage():

    print(classes[choice].getAverge())
    #Show the overall average
def overallAverage():
   pass


# wantQuit = False
classes =[]
menu()
# while not wantQuit:
#
#       menu()
#       if choice == 1:
#           addClass()
#       elif choice == 2:
#           addGrade()
#       elif choice == 3:
#           reviewGrade()
#       elif choice == 4:
#           editGrades()
#       elif choice == 5:
#           showAverage()
#       elif choice == 6:
#         want_Quit = True