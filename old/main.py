subjects = ["Maths","Cs","Physics","Biology"]
students = ["Ahmed", "Mostafa", "Ali","Bahaa","Nour"]
grades= [[90,95,80,61],[91,93,70,54],[60,80,75,30],[100,100,100,100],[60,50,40,20]]

def rowtotal(row):
    total = 0
    for col in range(len(grades[0])):
        total = total + grades[row][col]
    return total
def totalstu():
    for row in range(len(grades)):
            total = rowtotal(row)
            print("this student",students[row],"their total is",total)
def avg(n):
    avg = rowtotal(n)/len(grades[0])
    return avg

def Namesavg():
    for row in range(len(students)):
        print(students[row], avg(row))

def highestavg():
    largest = -1
    sturow = 0
    for row in range(len(grades)):
        av = avg(row)
        if int(av) > largest:
            largest = av
            sturow = row
    print("the student",students[sturow],"has the highest average of",largest)
def lowestavg():
    lowest=101
    x = 0
    for row in range(len(grades)):
        av = avg(row)
        if lowest > int(av):
            lowest = av
            x = row
    print("the student",students[x],"has the lowest average of",lowest)
def failed():
    for row in range(len(grades)):
        av= avg(row)
        if av < 60 :
            print("the student",students[row],"has an average of",av,"which is below passing grade")
def subavg(col):
    total = 0
    for row in range(len(grades)):
        total = grades[row][col] + total
    avg = total/ len(grades)
    return avg
def passsubj():
    for col in range (len(grades[0])):
       av = subavg(col)
       if av < 70:
        print("the subject",subjects[col],"has an average of",av)
def outstud():
    name = input("please enter a name")
    for i in range(len(grades)) :
        av = avg(i)
        if name == students[i]:
         print("the student",name, "has an average of",av)
def outsub():
    subject = input("please enter the name of the subject")
    for i in range(len(subjects)):
        av = subavg(i)
        if subject ==subjects[i]:
            print("the subject",subject,"has an average of",av)
command = input("please enter a command")
while command != "quit":
    if command == "total":
        totalstu()
    elif command == "report":
        Namesavg()
    elif command == "best":
        highestavg()
    elif command == "worst":
        lowestavg()
    elif command == "underperf":
        failed()
    elif command == "underperfteacher":
        passsubj()
    elif command == "onestudent" :
        outstud()
    elif command== "onesubject":
        outsub()
    command = input("please enter a new command")