#-------------------------------------------------------------------------------
# Author:      Steven Tran
#-------------------------------------------------------------------------------
from button import *
from graphics import *

# NOTES
    # I didn't get a chance to finish the assignment
    # I don't have it deleting a Student or Mark
    # I didn't get to the editing the student name (have it started, just doesn't do anything)
    # There is a Bug somewhere in my code which i don't know the root cause of it
        # It happens very randomly at times
        # Something to do with editing marks
        # If i had more time i would've dug deeper
    # didn't handle every error

# Draws the home menu of the Program
def MenuDraw():
    """Draws the GUI for the opening/Starting Menu"""
    win = GraphWin("Marks Manager", 400,400)
    win.setBackground("light blue")

    Intro = Text(Point(200,50), "Marks Manager")
    Intro.setSize(26)
    Intro.setFace("courier")
    Intro.setStyle("bold")
    Intro.draw(win)

    titleBorder = Rectangle(Point(15,15),Point(385,80))
    titleBorder.draw(win)

    titleBorder2 = Rectangle(Point(10,10), Point(390,85))
    titleBorder2.setWidth(5)
    titleBorder2.draw(win)

    author = Text(Point(200,388), "By: Steven Tran")
    author.setSize(10)
    author.setStyle("bold")
    author.draw(win)

    return win

def UndrawObjects(Objects):
    """Fucntion Used to undraw a given list of objects"""
    for i in Objects:
        i.undraw()
    Objects = []

    return Objects

# Function that writes to file!
def WriteToFile(CName,StudentsList,AssignmentList,MarksList,weights,file,filename):
    """Writes data into a file so that the user can open it once again"""
    # Closes the "r" file and re-opens it to be a "w" file so it overwrites the data
    file.close()
    file = open("{0}.txt".format(filename), "w")
    file.write(CName)
    file.write("\n")

    # Writes data to a file, sepereated by tildes
    Student = ""
    for name in StudentsList:
        Student = Student + name + "~"
    file.write(Student)
    file.write("\n")

    Assessment = ""
    for name in AssignmentList:
        Assessment = Assessment + name + "~"
    file.write(Assessment)
    file.write("\n")

    file.write(str(MarksList))
    file.write("\n")

    weight = ""
    for name in weights:
        weight = weight + str(name) + "~"
    file.write(weight)

    file.close()

def GUIdetails(win):
    """Adds details onto the window where the marks are displayed"""
    # Class name
    CourseName = Text(Point(375,40), "CLASS: ")
    CourseName.setStyle("bold")
    CourseName.setSize(20)
    CourseName.draw(win)

    # Adding nice features to the on-scree2n window
    border = Rectangle(Point(5,65), Point(745,595))
    border.setWidth(5)
    border.draw(win)
    divider1 = Line(Point(5, 100), Point(682,100))
    divider1.setWidth(5)
    divider1.draw(win)

    divider2 = Line(Point(5,140), Point(745,140))
    divider2.setWidth(5)
    divider2.draw(win)

    # Starting Coordinates
    x1 = 225
    y1 = 140
    x2 = 180
    y2 = 480
    y3 = 65

    for i in range(14):
        divider3 = Line(Point(x1,y1), Point(x1,y2))
        divider3.draw(win)

        divider4 = Line(Point(x1,y1), Point(x2,y3))
        divider4.draw(win)

        x1 += 40
        x2 += 40

    divider5 = Line(Point(5,480),Point(745,480))
    divider5.setWidth(5)
    divider5.draw(win)

    cover = Polygon(Point(700,65), Point(745,65), Point(743,135))
    cover.setFill("Black")
    cover.draw(win)

    divider6 = Line(Point(505,480), Point(505,595))
    divider6.setWidth(5)
    divider6.draw(win)

    divider7 = Line(Point(5,120),Point(695,120))
    divider7.draw(win)

    divider8 = Line(Point(5,451),Point(745,451))
    divider8.setWidth(3)
    divider8.draw(win)

    divider9 = Line(Point(705,140),Point(660,65))
    divider9.setWidth(3)
    divider9.draw(win)

    divider10 = Line(Point(705,140),Point(705,480))
    divider10.setWidth(5)
    divider10.draw(win)

    cover2 = Rectangle(Point(745,480),Point(705,450))
    cover2.setFill("black")
    cover2.draw(win)

    guide = Text(Point(102.5,85), "Assessments: ")
    guide.setStyle("bold")
    guide.setSize(16)
    guide.draw(win)

    heading1 = Text(Point(102.5,110), "Weighting: ")
    heading1.draw(win)

    heading2 = Text(Point(102.5,130),"Out of: ")
    heading2.draw(win)

    heading3 = Text(Point(115,467), "Average score/Assignment:")
    heading3.setSize(11)
    heading3.setStyle("bold")
    heading3.draw(win)

    box = Rectangle(Point(10,485), Point(501,590))
    box.setFill("Black")
    box.setWidth(2)
    box.draw(win)

    legend_title = Text(Point(80,500), "LEGEND")
    legend_title.setTextColor("White")
    legend_title.setStyle("bold")
    legend_title.setSize(20)
    legend_title.setFace("courier")
    legend_title.draw(win)

    return CourseName

def error_message_draw(win,text):
    """Draws a rectangle with an error message onto the screen when the user puts in an invalid input"""
    temp =[]
    warning1 = Rectangle(Point(5,120), Point(195,220))
    warning1.setFill("red")
    warning1.draw(win)
    temp.append(warning1)

    warning2 = Rectangle(Point(10,125), Point(190,215))
    warning2.setFill("white")
    warning2.draw(win)
    temp.append(warning2)

    warningText = Text(Point(100,160), "{0}".format(text))
    warningText.draw(win)
    temp.append(warningText)

    warningText1 = Text(Point(100,200),"click anywhere to close")
    warningText1.setSize(9)
    warningText1.draw(win)
    temp.append(warningText1)

    win.getMouse()
    UndrawObjects(temp)

def Rearrange_Marks(Assignment,Marks):
    """Rearranges the list of marks so that they are in accordance to assignments (rather than student)"""
    MarksPerAssign = []
    # Sorting the Assignment marks so that they are grouped together by assignment
    for i in range(len(Assignment)//4):
        templist = []
        # Algorithm to find the category within the list of assignment
        CodeNum = Assignment[(i*4)+3]
        if CodeNum == "TE":
            MarksPerAssign = AssignmentSort(i,Assignment,Marks,templist,MarksPerAssign)
        elif CodeNum == "AS":
            MarksPerAssign = AssignmentSort(i,Assignment,Marks,templist,MarksPerAssign)

        elif CodeNum == "IS":
            MarksPerAssign = AssignmentSort(i,Assignment,Marks,templist,MarksPerAssign)

        elif CodeNum == "SU":
            MarksPerAssign = AssignmentSort(i,Assignment,Marks,templist,MarksPerAssign)

        else: pass

    return MarksPerAssign

def AssignmentSort(i,Assignment,Marks,templist,MarksPerAssign):
    """Helper function that assists with the re-arranging for Marks, in accordance to assignments"""
    # finding the index of the first index (no other way to go about this problem)
    if i == 0:
        array = Assignment[0:4]
    # Algorithm used to find the needed indexes
    else:
        array = Assignment[i*4:(i*4)+4]

    for index in range(len(Assignment)//4):
        if array == Assignment[index*4:(index*4)+4]:
            for mark in Marks:
                try:
                    templist.append(mark[index])
                except IndexError:
                    pass
            MarksPerAssign.append(templist)

    return MarksPerAssign

def Calculate_Marks(weights,Assignment,Marks):
    """ A function that calculates the average of a student """
    # MAIN  WEIGHTS
    MainWeights_List = []

    # Appending the Main Assessment weights (the overal weights)
    MainWeights_List.append(float(weights[0]))
    MainWeights_List.append(float(weights[1]))
    MainWeights_List.append(float(weights[2]))
    MainWeights_List.append(float(weights[3]))

    # Total overall weights
    TotalMainWeights = 0
    for i in MainWeights_List:
        TotalMainWeights += float(i)

    # Lists used in later calculations
    assessment_type = []
    assessment_weight = []
    assessment_Outof = []
    Horizontal_Average = []
    Vertical_Average = []

    # Getting the category of the Assessments
    for i in range(len(Assignment)//4):
        assessment_type.append(Assignment[(i*4)+3])

    # May change Later
    MarksPerAssign = Rearrange_Marks(Assignment,Marks)

    # Retrieving the weights of each assessment
    for i in range(len(Assignment)//4):   # Only getting it 4 times??? instead of 5 ~ Class name is named "IS"...
        assessment_weight.append(Assignment[(i*4)+1])

    # Getting Out of Mark
    for i in range(len(Assignment)//4):
        assessment_Outof.append(Assignment[(i*4)+2])

    # Grouping all the weights into thier repective lists (according to category of weight)
    total_test_weight = []
    total_assignment_weight = []
    total_IS_weight = []
    total_summative_weight = []
    index = 0
    for i in assessment_type:
        if i == "TE":
            total_test_weight.append(assessment_weight[index])
        elif i == "AS":
            total_assignment_weight.append(assessment_weight[index])
        elif i == "IS":
            total_IS_weight.append(assessment_weight[index])
        else:
            total_summative_weight.append(assessment_weight[index])
        index += 1

    # Finding the sum of the respective weights
    TestWeightTotal = 0
    for i in range(len(total_test_weight)):
        TestWeightTotal += int(total_test_weight[i])

    AssignmenttWeightTotal = 0
    for i in range(len(total_assignment_weight)):
        AssignmenttWeightTotal += int(total_assignment_weight[i])

    ISWeightTotal = 0
    for i in range(len(total_IS_weight)):
        ISWeightTotal += int(total_IS_weight[i])

    SumWeightTotal = 0
    for i in range(len(total_summative_weight)):
        SumWeightTotal += int(total_summative_weight[i])

    # getting the overall respective weights
    TotalWeight = []
    TotalWeight.append(TestWeightTotal)
    TotalWeight.append(AssignmenttWeightTotal)
    TotalWeight.append(ISWeightTotal)
    TotalWeight.append(SumWeightTotal)

    # Finding the numerator for the individual category calculations
    categoryList = []
    for i in Marks:
        templist = []
        category = []
        for singlemark in i:
            if singlemark != "nr":
                index1 = i.index(singlemark)
                temp = (float(singlemark)/float(assessment_Outof[index1]))*float(assessment_weight[index1])
                templist.append(temp)
                category.append(assessment_type[index1])

    Vertical_Average.append(templist)
    categoryList.append(category)

    # Sorting the marks to thier respective categories
    Category = []
    templist = [[],[],[],[]]
    accum = -1
    for code in categoryList:
        for mark in Vertical_Average:
            for singlemark in mark:
                accum += 1
                if code[accum] == "TE":
                    templist[0].append(singlemark)
                elif code[accum] == "AS":
                    templist[1].append(singlemark)
                elif code[accum] == "IS":
                    templist[2].append(singlemark)
                else:
                    templist[3].append(singlemark)
            Category.append(templist)

    numerator = []
    for i in Category:
        templist = []
        for j in i:
            temp = 0
            for mark in j:
                temp += mark
            templist.append(temp)
        numerator.append(templist)

    temp = 0
    AverageByCategory = []
    # Getting the average per section
    for score in numerator:
        templist = []
        for j in range(4):
            try:
                temp = score[j] / TotalWeight[j]
                templist.append(temp)
            except ZeroDivisionError:
                templist.append(0)
        AverageByCategory.append(templist)

    # Calculating the final Numerator for the overall Calculation
    OverallNumerator = []
    for i in AverageByCategory:
        templist = []
        for j in range(4):
            temp = float(i[j]) * float(weights[j])
            templist.append(temp)
        OverallNumerator.append(templist)

    calculation = []
    temp = 0
    # Calculating for the final average
    for i in OverallNumerator:
        templist = []
        for j in range(4):
            try:
                temp = i[j] / TotalMainWeights
                templist.append(temp)
            except ZeroDivisionError:
                templist.append(0)
        calculation.append(templist)

    # Adding all the individual averages together to get the FINAL average
    finalAverage = []
    finalMark = 0
    for i in calculation:
        for mark in i:
            finalMark += mark
        finalMark = finalMark * 100
        finalAverage.append(finalMark)

    return finalAverage

def editor_main_menu(win, Objects, CName, weights):
    """Editor Main Menu"""
    # Buttons
    Menubutton = Button(win,Point(50,360),75,50,"white","Back to \nMenu")
    Menubutton.activate()
    Objects.append(Menubutton)
    UpdateButton = Button(win,Point(150,360),75,50,"white","Update")
    UpdateButton.activate()
    Objects.append(UpdateButton)

    # Heading + Entry Boxes ~ Class name
    heading1 = Text(Point(70,30), "Enter Class Name: ")
    heading1.setSize(10)
    heading1.setStyle("bold")
    heading1.draw(win)
    Objects.append(heading1)

    enterClass = Entry(Point(100,50),20)
    enterClass.setFill("white")
    enterClass.setText(CName)
    enterClass.draw(win)
    Objects.append(enterClass)

    # Buttons for the second window that provide the user with options to change information
    AddStudent = Button(win,Point(100,110),180,50,"White", "Add Students")
    AddStudent.activate()
    Objects.append(AddStudent)

    EditMark = Button(win,Point(100,170),180,50,"White","Edit Student Marks")
    EditMark.activate()
    Objects.append(EditMark)

    AddAssign = Button(win,Point(100,230),180,50,"white","Add Assessment")
    AddAssign.activate()
    Objects.append(AddAssign)

    # Headings + entry boxes for the assessment weighting
    heading2 = Text(Point(27,280), "TE")
    heading2.draw(win)
    Test_Entry = Entry(Point(27,300),3)
    Test_Entry.setFill("White")
    Test_Entry.setText(weights[0])
    Test_Entry.draw(win)
    Objects.append(Test_Entry)
    Objects.append(heading2)

    heading3 = heading2.clone()
    heading3.move(50,0)
    heading3.setText("AS")
    heading3.draw(win)
    Assignment_Entry = Test_Entry.clone()
    Assignment_Entry.setText(weights[1])
    Assignment_Entry.move(50,0)
    Assignment_Entry.draw(win)
    Objects.append(Assignment_Entry)
    Objects.append(heading3)

    heading4 = heading3.clone()
    heading4.move(50,0)
    heading4.setText("IS")
    heading4.draw(win)
    IS_Entry = Assignment_Entry.clone()
    IS_Entry.setText(weights[2])
    IS_Entry.move(50,0)
    IS_Entry.draw(win)
    Objects.append(IS_Entry)
    Objects.append(heading4)

    heading5 = heading4.clone()
    heading5.move(50,0)
    heading5.setText("SUM")
    heading5.draw(win)
    Summative_Entry = IS_Entry.clone()
    Summative_Entry.setText(weights[3])
    Summative_Entry.move(50,0)
    Summative_Entry.draw(win)
    Objects.append(Summative_Entry)
    Objects.append(heading5)

    return Objects,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry

def AddButtonDraw(Objects,win,text):
    """Draws a Button for adding stuff"""
    AddButton = Button(win,Point(150,350),90,50,"green","Add\n{0}".format(text))
    AddButton.activate()
    Objects.append(AddButton)

    return Objects, AddButton, win

def CancelButtonDraw(Objects,win):
    """Draws a button to cancel/go back"""
    cancelButton = Button(win,Point(50,350),90,50,"red","Back")
    cancelButton.activate()
    Objects.append(cancelButton)

    return Objects ,cancelButton, win

def AddStudentGUI(ObjectsWin2, win2):
    """GUI for adding students"""
    ObjectsWin2 = UndrawObjects(ObjectsWin2)
    heading1 = Text(Point(90,30), "Enter Student First Name: ")
    heading1.setSize(10)
    heading1.setStyle("bold")
    heading1.draw(win2)
    ObjectsWin2.append(heading1)

    # Headings + entry boxes for First and Last Name
    fname_entry = Entry(Point(100,50),20)
    fname_entry.setFill("white")
    fname_entry.draw(win2)
    ObjectsWin2.append(fname_entry)

    heading2 = heading1.clone()
    heading2.setText("Enter Student Last Name: ")
    heading2.move(0,50)
    heading2.draw(win2)
    ObjectsWin2.append(heading2)

    lname_entry = fname_entry.clone()
    lname_entry.move(0,50)
    lname_entry.draw(win2)
    ObjectsWin2.append(lname_entry)

    # Drawing add and cancel button
    ObjectsWin2, AddButton, win2 = AddButtonDraw(ObjectsWin2, win2,"Student")
    ObjectsWin2, cancelButton,win2 = CancelButtonDraw(ObjectsWin2, win2)

    return ObjectsWin2, fname_entry, lname_entry, AddButton, cancelButton

# Creates the student Button
def StudentChoice(win2,ObjectsWin2,StudentsList,StudentButtons):
    """Function that draws buttons with Student names on them"""
    tempx = 100
    tempy = 30

    for i in range(len(StudentsList)):
        # Makes the student.Dictionary
        studentName = StudentsList[i]
        SBUTTON = Button(win2,Point(tempx,tempy),150,20,"White",studentName)
        SBUTTON.activate()
        StudentButtons.append(SBUTTON)
        tempy += 30

    # CLOSE BUTTON
    ObjectsWin2, cancelButton,win2 = CancelButtonDraw(ObjectsWin2, win2)

    return StudentButtons,ObjectsWin2,cancelButton

def GetInfo(MarksList,MarkEntryBox_Object,LastName,FirstName,num):
    """Function used to get the neccessary information for Marks"""
    temp = []

    for value in MarkEntryBox_Object:
        mark = value.getText()
        if mark == "":
            temp.append("nr")
        else:
            if mark == "nr":
                temp.append("nr")
            else:
                temp.append(float(mark))

    MarksList[num] = temp
    return MarksList,MarkEntryBox_Object

def StudentEditGUI(win2,click,AssignmentList,MarkEntryBox_Object,tempbox,x,MarksList):
    """GUI for adding Marks for Students"""
    name = click.getLabel()
    name = name.split(",")
    LastName = name[0]
    FirstName = name[1][1:]  # Getting rid of space at the beginning

    # Entry Box + Heading for First and Last Name of student
    fname_entry = Entry(Point(100,40),20)
    fname_entry.setFill("white")
    fname_entry.setText(FirstName)
    fname_entry.draw(win2)
    heading1 = Text(Point(45,20),"First Name:")
    heading1.setSize(10)
    heading1.draw(win2)
    tempbox.append(fname_entry)
    tempbox.append(heading1)

    lname_entry = fname_entry.clone()
    lname_entry.move(0,40)
    lname_entry.setText(LastName)
    lname_entry.draw(win2)
    heading2 = heading1.clone()
    heading2.move(0,40)
    heading2.setText("Last Name:")
    heading2.draw(win2)
    tempbox.append(heading2)
    tempbox.append(lname_entry)

    heading3 = heading2.clone()
    heading3.move(0,50)
    heading3.setText("Assignments:")
    heading3.draw(win2)
    tempbox.append(heading3)

    temp = ""
    tempx = 60
    tempy = 140
    # drawing the entry box for editing the marks of each student
    for i in range(len(AssignmentList)//4):
        assignment = Text(Point(tempx-40, tempy), "{0:2}:".format(i+1))
        assignment.setSize(16)
        assignment.setStyle("bold")
        assignment.draw(win2)
        tempbox.append(assignment)

        temp = "Entry{0}".format(i)
        temp = Entry(Point(tempx,tempy),4)
        temp.setFill("white")
        try:
            temp.setText(MarksList[x][i])
        except IndexError:
            temp.setText("nr")

        temp.draw(win2)

        MarkEntryBox_Object.append(temp)
        tempy += 30

        if tempy == 320:
            tempy = 140
            tempx += 110

    return fname_entry,lname_entry,tempbox,MarkEntryBox_Object, LastName, FirstName

def AddAssignmentGUI(win2,ObjectsWin2,FieldButtons):
    """GUI for adding the assignments"""
    ObjectsWin2 = UndrawObjects(ObjectsWin2)
    heading1 = Text(Point(90,30), "Enter Assignment Name: ")
    heading1.setSize(10)
    heading1.setStyle("bold")
    heading1.draw(win2)
    ObjectsWin2.append(heading1)

    assignment_entry = Entry(Point(100,50),20)
    assignment_entry.setFill("White")
    assignment_entry.draw(win2)
    ObjectsWin2.append(assignment_entry)

    heading2 = heading1.clone()
    heading2.setText("Assessment Weighting:")
    heading2.move(-8,50)
    heading2.draw(win2)
    ObjectsWin2.append(heading2)

    weighting_entry = assignment_entry.clone()
    weighting_entry.move(0,50)
    weighting_entry.draw(win2)
    ObjectsWin2.append(weighting_entry)

    heading3 = heading2.clone()
    heading3.setText("Mark Out of:")
    heading3.move(-33,50)
    heading3.draw(win2)
    ObjectsWin2.append(heading3)

    MarkOutOf_entry = weighting_entry.clone()
    MarkOutOf_entry.move(0,50)
    MarkOutOf_entry.draw(win2)
    ObjectsWin2.append(MarkOutOf_entry)

    heading4 = heading3.clone()
    heading4.setText("Field:")
    heading4.move(-22,50)
    heading4.draw(win2)
    ObjectsWin2.append(heading4)

    TestField = Button(win2,Point(50,220),90,50,"white","Test")
    TestField.activate()
    FieldButtons.append(TestField)

    AssignmentField = Button(win2, Point(50,285),90,50,"white", "Assignment")
    AssignmentField.activate()
    FieldButtons.append(AssignmentField)

    ISfield = Button(win2, Point(150,220),90,50,"white","Independant\nStudy")
    ISfield.activate()
    FieldButtons.append(ISfield)

    SummativeField = Button(win2, Point(150,285),90,50,"white","Summative")
    SummativeField.activate()
    FieldButtons.append(SummativeField)

    ObjectsWin2, AddButton, win2 = AddButtonDraw(ObjectsWin2, win2,"Assessment")
    ObjectsWin2, cancelButton,win2 = CancelButtonDraw(ObjectsWin2, win2)

    return ObjectsWin2,assignment_entry,weighting_entry,MarkOutOf_entry,FieldButtons,AddButton,cancelButton

def Student_Draw(win,StudentsList,studentNum,Student_Objects):
    """Function used to draw the students info onto the window"""
    studentNum += 1
    for i in range(len(StudentsList)):
        name = StudentsList[i]

        NameInsert = Text(Point(115, 157 + (31*i)), name)
        NameInsert.setSize(12)
        NameInsert.setStyle("bold")
        NameInsert.draw(win)
        Student_Objects.append(NameInsert)

        divide_student = Text(Point(375, 169 + (31*i)), "-" * 82)
        divide_student.setSize(20)
        divide_student.draw(win)

        StudentNo = Text(Point(25, 157 + (31*i)), "{0:^2}.".format(i + 1))
        StudentNo.setSize(14)
        StudentNo.setStyle("bold")
        StudentNo.draw(win)

    return studentNum,Student_Objects

def GetStudentName(win,fname_entry,lname_entry,studentNum,StudentsList,MarksList):
    """Function used to get the First and Last name of the student"""
    if studentNum >= 9:
        error_message_draw(win,"Unable to Add Student\nMaximum Number of \nStudents Reached!")

        # "Refreshes page"
        fname_entry.setText("")
        lname_entry.setText("")

    else:
        fname = fname_entry.getText()
        lname = lname_entry.getText()
        if fname == "" or lname == "":
            error_message_draw(win,"Please Input\nA valid Student Name")
        else:
            MarksList.append([])
            name = lname + ", " + fname

            # Appends to a full list of student names
            StudentsList.append(name)

            # "Refreshes page"
            fname_entry.setText("")
            lname_entry.setText("")

    return StudentsList, studentNum, MarksList

def Mark_Draw(win,MarksList,AssignmentList,weights,Mark_Objects):
    """A function used to draw the mark onto the screen"""
    x1 = 245 # right by 40
    y1 = 155 # down by 30
    tempx =-1
    tempy = -1

    FinalAverages = []
    for i in range(len(MarksList)):
        Marks = []
        temp = MarksList[i]
        Marks.append(temp)
        finalaverage = Calculate_Marks(weights,AssignmentList,Marks)
        FinalAverages.append(finalaverage)
    print(FinalAverages)

    # getting the averages score
    Average_assign = calc_assignemnt_average(AssignmentList,MarksList)

    for Student in MarksList:
        tempy +=1
        tempx = -1
        for Mark in Student:
            tempx += 1
            insertMark = Text(Point(x1+(40*tempx), y1+(31*tempy)), Mark)
            insertMark.draw(win)
            Mark_Objects.append(insertMark)

    for i in range(len(FinalAverages)):
        for average in FinalAverages[i]:
            Final = Text(Point(725,y1+(31*i)), "%.1f" % round(average,1))
            Final.setStyle("bold")
            Final.draw(win)
            Mark_Objects.append(Final)

    for i in range(len(Average_assign)):
        try:
            insertaverage = Text(Point(x1+(40*i),464), "%.1f" % round(Average_assign[i],1))
            insertaverage.setStyle("bold")
            insertaverage.draw(win)
            Mark_Objects.append(insertaverage)
        except TypeError:
            pass

    return Mark_Objects

def calc_assignemnt_average(Assignment,Marks):
    """A Function used to calculate the average mark on the assignment"""
    MarksPerAssign = Rearrange_Marks(Assignment,Marks) # Assignmentlist and MarksList

    Horizontal_Average = []
    total = []
    real = 0
    denominator = []
    for i in MarksPerAssign:
        temp = 0
        real = 0
        for marks in i:
            if marks == "nr":
                pass
            else:
                real += 1
                temp += int(marks)
        total.append(temp)
        denominator.append(real)

    for i in range(len(total)):
        if denominator[i] == 0:
            Horizontal_Average.append("nr")
        else:
            Horizontal_Average.append(total[i] / denominator[i])

    return Horizontal_Average

def Assignment_Draw(win,AssignmentList,assignNum,AnchorX,AnchorY,Assignment_Objects):
    """A function used to draw the assignments onto the screen"""
    temp = 0
    for i in range(len(AssignmentList)//4):
        # Getting the right indexes for each item in the list
        AssignName = AssignmentList[4*i]
        weight = AssignmentList[(4*i)+1]
        Outof = AssignmentList[(4*i)+2]
        category = AssignmentList[(4*i)+3]

        # Draws the tab number
        tabNum = Text(Point(208 +(40*i),78), str(i+1))
        tabNum.setFace("helvetica")
        tabNum.setSize(18)
        tabNum.setStyle("bold")
        tabNum.draw(win)
        Assignment_Objects.append(tabNum)

        # Draws the category that the assessment is under
        code = Text(Point(212 +(40*i),92),category)
        code.setSize(9)
        code.draw(win)
        Assignment_Objects.append(code)

        # Draws the weight of the assessment on to the screen
        weighting = Text(Point(230 +(40*i),111),weight)
        weighting.setSize(12)
        weighting.draw(win)
        Assignment_Objects.append(weighting)

        # Draws the Out-of mark on to the screen
        MarkOutOf = Text(Point(236 +(40*i),130),Outof)
        MarkOutOf.setSize(11)
        MarkOutOf.setStyle("bold")
        MarkOutOf.draw(win)
        Assignment_Objects.append(MarkOutOf)

        assignNum += 1

        # Draws the assessment name under the legend box
        legend = Text(Point(AnchorX,AnchorY + temp), "{0}".format(str(i+1) + ". " + AssignName))
        legend.setSize(10)
        legend.setTextColor("white")
        legend.draw(win)
        Assignment_Objects.append(legend)

        if (AnchorX == 100 and (temp + AnchorY == 580)) or (AnchorX == 250 and (temp + AnchorY == 580)):
            AnchorX += 150
            temp = 0
        else:
            temp += 20

    return Assignment_Objects

# Function that gets the neccessary variables and appends it to a list for storing
def GetAssignName(assignment_entry,weighting_entry,MarkOutOf_entry,category,assignNum,AssignmentList):
    """A Function that basically runs this whole program"""
    AssignName = assignment_entry.getText()
    AssignmentList.append(AssignName)
    assignment_entry.setText("")

    AssignWeight = weighting_entry.getText()
    AssignmentList.append(AssignWeight)
    weighting_entry.setText("")

    AssignOutOf = MarkOutOf_entry.getText()
    AssignmentList.append(AssignOutOf)
    MarkOutOf_entry.setText("")

    if category == "Test":
        code = "TE"
    elif category == "Assignment":
        code = "AS"
    elif category == "Independant\nStudy":
        code = "IS"
    else:
        code = "SU"
    AssignmentList.append(code)

    return AssignmentList

# Function that draws the GUI for the actual Marks manager
def MarksManagerGUI(ObjectsWin2, file,filename,CName,StudentsList,AssignmentList,MarksList,weights):
    win = GraphWin("Marks Manager", 750,600)
    win.setBackground("light blue")

    assignNum = len(AssignmentList) + 1
    AnchorX = 100
    AnchorY = 520
    studentNum = len(StudentsList) - 1
    StudentButtons = []
    FieldButtons = []

    Student_Objects = []
    Assignment_Objects = []
    Mark_Objects = []
    MarkEntryBox_Object = []

    CourseName = GUIdetails(win)

    # Second Graphical Window
    win2 = GraphWin("Editor", 200,400)
    win2.setBackground("sky blue")

    # Draws the Main menu for the editing window ~ Returns needed buttons to the main()
    ObjectsWin2,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry = editor_main_menu(win2, ObjectsWin2, CName, weights)

    # Different Modes/states for the second window

    editmode = Button(win,Point(680,540),100,75,"White", "Edit Mode")

    infomode = Button(win,Point(570,540),100,75,"white","Information\n Mode")
    infomode.activate()

    # Start-Up
    if len(StudentsList) > 0:
        CourseName.setText("CLASS: {0}".format(CName))
        studentNum,Student_Objects = Student_Draw(win,StudentsList,studentNum,Student_Objects)
        Assignment_Objects = Assignment_Draw(win,AssignmentList,assignNum,AnchorX,AnchorY,Assignment_Objects)
        Mark_Objects = Mark_Draw(win,MarksList,AssignmentList,weights,Mark_Objects)
        Test_Entry.setText(weights[0])
        Assignment_Entry.setText(weights[1])
        IS_Entry.setText(weights[2])
        Summative_Entry.setText(weights[3])

    while True:
        # Checks to see if the Mouse is in either the first window or the second window
        winClick = win.checkMouse()
        win2click = win2.checkMouse()

        # If the mouse is in the 2nd window, then it executes the code inside the if-statement
        if win2click != None:
            # Goes back to the main menu by rebooting Main()
            if Menubutton.clicked(win2click):
                win.close()
                win2.close()
                WriteToFile(CName,StudentsList,AssignmentList,MarksList,weights,file,filename)
                main()

            elif UpdateButton.clicked(win2click):
            # Gets the users input (Get it so that it can print the input once the user presses enter)
                weights[0] = Test_Entry.getText()
                weights[1] = Assignment_Entry.getText()
                weights[2] = IS_Entry.getText()
                weights[3] = Summative_Entry.getText()
                CName = enterClass.getText()
                CourseName.setText("CLASS: {0}".format(CName))
#----------------------------------------------------------------------------------------------------------------------------1. Adding Students---------------------------------------
            elif AddStudent.clicked(win2click):
                ObjectsWin2, fname_entry, lname_entry, AddButton, cancelButton = AddStudentGUI(ObjectsWin2,win2)
                temp = True
                while temp == True:
                    p = win2.getMouse()
                    if AddButton.clicked(p):
                        StudentsList, studentNum, MarksList = GetStudentName(win2,fname_entry,lname_entry,studentNum,StudentsList, MarksList)
                        Student_Objects = UndrawObjects(Student_Objects)
                        studentNum, Student_Objects = Student_Draw(win,StudentsList,studentNum,Student_Objects)

                    elif cancelButton.clicked(p):
                        ObjectsWin2 = UndrawObjects(ObjectsWin2)
                        ObjectsWin2,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry =  editor_main_menu(win2, ObjectsWin2, CName, weights)
                        temp = False

                    else: True
#-----------------------------------------------------------------------------------------------------------------------------2. Editing Marks---------------------------------------
            elif EditMark.clicked(win2click):
                ObjectsWin2 = UndrawObjects(ObjectsWin2)
                MarkEntryBox_Object = [] # temporary fix in clearing list
                StudentButtons,ObjectsWin2,cancelButton = StudentChoice(win2,ObjectsWin2,StudentsList,StudentButtons)
                ObjectsWin2, AddButton, win2= AddButtonDraw(ObjectsWin2,win2,"Changes")
                temp = True
                tempbox = []
                x = 0 # Variable to tell which button was clicked
                while temp == True:
                    p = win2.getMouse()
                    num = -1   #Accumulator used to to tell which Student Button was clicked
                    # Checks to see if any of the student Buttons were clicked
                    for click in StudentButtons:
                        num += 1
                        if click.clicked(p):
                            x = num
                            print(x)
                            StudentButtons = UndrawObjects(StudentButtons)
                            fname_entry,lname_entry,tempbox,MarkEntryBox_Object, LastName, FirstName = StudentEditGUI(win2,click,AssignmentList,MarkEntryBox_Object,tempbox,x,MarksList)
                    if AddButton.clicked(p):
                        MarksList,MarkEntryBox_Object = GetInfo(MarksList,MarkEntryBox_Object,LastName,FirstName,x)
                        Mark_Objects = UndrawObjects(Mark_Objects)
                        Mark_Objects = Mark_Draw(win,MarksList,AssignmentList,weights,Mark_Objects)

                    elif cancelButton.clicked(p):
                        UndrawObjects(MarkEntryBox_Object)
                        tempbox = UndrawObjects(tempbox)
                        UndrawObjects(StudentButtons)
                        ObjectsWin2 = UndrawObjects(ObjectsWin2)
                        ObjectsWin2,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry =  editor_main_menu(win2, ObjectsWin2, CName, weights)
                        temp = False
                    else:True
#---------------------------------------------------------------------------------------------------------------------------3. Adding Assignments-------------------------------------
            elif AddAssign.clicked(win2click):
                ObjectsWin2,assignment_entry,weighting_entry,MarkOutOf_entry,FieldButtons,AddButton,cancelButton = AddAssignmentGUI(win2,ObjectsWin2,FieldButtons)

                temp = True
                category = ""
                # Adding NEW assignments
                while temp == True:
                    p = win2.getMouse()
                    # Looks at which category the assessment is under!
                    for field in FieldButtons:
                        if field.clicked(p):
                            field.setFill("grey")
                            category = field.getLabel()
                        else:
                            field.setFill("White")

                    if AddButton.clicked(p):
                        for field in FieldButtons:
                            field.setFill("White")
                        if len(AssignmentList) <= 44:
                            print(AssignmentList)
                            AssignmentList = GetAssignName(assignment_entry,weighting_entry,MarkOutOf_entry,category,assignNum,AssignmentList)

                            Assignment_Objects = UndrawObjects(Assignment_Objects)
                            Assignment_Objects = Assignment_Draw(win,AssignmentList,assignNum,AnchorX,AnchorY,Assignment_Objects)
                        else:
                            ObjectsWin2 = UndrawObjects(ObjectsWin2)
                            FieldButtons = UndrawObjects(FieldButtons)
                            error_message_draw(win2,"Unable to add assignment\nMaximum Number of \nAssignments Reached!")
                            ObjectsWin2,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry =  editor_main_menu(win2, ObjectsWin2, CName, weights)
                            temp = False
                    elif cancelButton.clicked(p):
                        ObjectsWin2 = UndrawObjects(ObjectsWin2)
                        FieldButtons = UndrawObjects(FieldButtons)
                        ObjectsWin2,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry =  editor_main_menu(win2, ObjectsWin2, CName, weights)
                        temp = False
                    else: True
            else: True
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # If the mouse is in the 1st window, then it executes the code inside the if-statement
        if winClick != None:
            if infomode.clicked(winClick):
                infomode.deactivate()
                editmode.activate()
                UndrawObjects(ObjectsWin2)
            elif editmode.clicked(winClick):
                editmode.deactivate()
                infomode.activate()
                ObjectsWin2,Menubutton,UpdateButton,AddStudent,EditMark,AddAssign,enterClass,Test_Entry,Assignment_Entry,IS_Entry,Summative_Entry = editor_main_menu(win2, ObjectsWin2, CName, weights)
            else:
                True

def HelpMenu():
    """A Function Used to create the window for the help menu"""
    win = GraphWin("Help Menu", 300,400)
    Document = Text(Point(150,30), "HELP")
    Document.setSize(20)
    Document.setStyle("bold")
    Document.draw(win)
    underline = Line(Point(105,43), Point(195,43))
    underline.setWidth(2)
    underline.draw(win)

    text = Text(Point(150,150),"Sorry Mr. Sej, I did not get a chance \nto start the Help Menu\n\n\t\t~ Steven Tran")
    text.draw(win)

    win.getMouse()
    win.close()

def main():
    # Array that stores Graphical Objects ~ Makes it easier to undraw certain Graphical Objects
    ObjectsWin2 = []

    win = MenuDraw()

    Create_Class = Button(win,Point(200,130),380,50,"white","Create a New Class")
    Create_Class.activate()

    open_Class = Button(win,Point(200,200),380,50,"white","Open an existing Class")
    open_Class.activate()

    Documentation = Button(win,Point(200,270),380,50,"white","Help")
    Documentation.activate()

    qbutton = Button(win,Point(200,340),280,60,"white", "Quit")
    qbutton.activate()

    while True:
        p = win.getMouse()
        # Creating a New Class
        if Create_Class.clicked(p):
            CName = ""
            StudentsList = []
            AssignmentList = []
            MarksList = []
            weights = [50,20,10,20]
            filename = input("What should the file name be called:  ")
            file = open("{0}.txt".format(filename.upper()), "w")
            win.close()
            MarksManagerGUI(ObjectsWin2, file,filename,CName,StudentsList,AssignmentList,MarksList,weights)

        # Opening an Existing Class
        elif open_Class.clicked(p):
            try:
                filename = input("What is the name of the file? (Do not put any extensions at the end (ex. '.txt', '.dat', etc))")
            except KeyboardInterrupt:
                continue
            try:
                file = open("{0}.txt".format(filename.upper()), "r")
                # Gets the class name
                CName = file.readline()
                CName = CName[:-1]

                # Gets Student List
                StudentsList = file.readline()
                StudentsList = StudentsList.split("\n")
                StudentsList = StudentsList[0][:-1]
                StudentsList = StudentsList.split("~")

                AssignmentList = file.readline()
                AssignmentList = AssignmentList.split("\n")
                AssignmentList = AssignmentList[0][:-1]
                AssignmentList = AssignmentList.split("~")

                # gets Marks List
                MarksList = file.readline()
                MarksList = MarksList[:-1]
                MarksList = eval(MarksList)

                # Gets weighting for each category
                weights = file.readline()
                weights = weights.split("~")
                weights = weights[:-1]

                win.close()
                MarksManagerGUI(ObjectsWin2,file,filename,CName,StudentsList,AssignmentList,MarksList,weights)

            except IOError:
                errorBox = Rectangle(Point(10,120),Point(390,320))
                errorBox.setFill("white")
                errorBox.setWidth(6)
                errorBox.draw(win)
                win.getMouse()
                errorBox.undraw()

        elif Documentation.clicked(p):
            HelpMenu()
        elif qbutton.clicked(p):
            win.close()
            exit()
        else:
            True
main()