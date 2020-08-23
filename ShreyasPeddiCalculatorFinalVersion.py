#Programmer Name: Shreyas Peddi
#Date:2019/05/23
#Program Description:

#-------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

global equation
equation=''

#-------------------------------------------------------------------------------------------------
#DISPLAYING METHODS

#
def displayScreenBlank():
    labelOuput=tk.Label(mainWindow,text='',fg='white',anchor='e',
                        )
    labelOutput.place(x=25,y=25,width=350,height=75)


def displayScreen():
    
    labelOutput=tk.Label(mainWindow,text=equation,anchor='e',
                         fg='orange red',
                         bg='midnight blue',
                         font='Arial 22 bold')
    labelOutput.place(x=25,y=25,width=350,height=75)

def displayScreenTrig(words):
    
    labelOutput=tk.Label(mainWindow,text=words,anchor='e',
                         fg='orange red',
                         bg='midnight blue',
                         font='Arial 22 bold')
    labelOutput.place(x=25,y=25,width=350,height=75)



def displayScreenAnswer(ans):
    labelOutput=tk.Label(mainWindow,text=ans,anchor='e',
                         fg='orange red',
                         bg='midnight blue',
                         font="Arial 22 bold")
    labelOutput.place(x=25,y=25,width=350,height=75)

#-------------------------------------------------------------------------------------------------
#TRIGNOMETRIC OPERATIONS METHODS
def tanOperation(pos):
    global equation
    angle=0
    numOfRadians=0
    tanValue=0
    
    angle=float(equation[pos:len(equation)])
    equation=equation[pos+1:len(equation)]
    numOfRadians=math.radians(angle)
    print("NUM OF RAD",numOfRadians)
    tanValue=math.tan(numOfRadians)
    displayScreenAnswer(format(tanValue,'.4f'))
    print('answer:',tanValue)
    convertToString(tanValue)

def sinOperation(pos):
    global equation
    angle=0
    numberOfRadians=0
    sinValue=0
    
    angle=float(equation[pos:len(equation)])
    #equation=equation[pos+1:len(equation)]
    numOfRadians=math.radians(angle)
    #print("NUM OF RAD",numOfRadians)
    sinValue=math.sin(numOfRadians)
    displayScreenAnswer(format(sinValue,'.4f'))
    print('answer:',sinValue)
    convertToString(sinValue)

def cosOperation(pos):
    global equation
    angle=0
    numOfRadians=0
    cosValue=0
    
    angle=float(equation[pos:len(equation)])
    #equation=equation[pos:len(equation)]
    print("NUM OF RAD",numOfRadians)
    numOfRadians=math.radians(angle)
    cosValue=math.cos(numOfRadians)
    displayScreenAnswer(format(cosValue,'.4f'))
    print('answer:',cosValue)
    convertToString(cosValue)
    
#-------------------------------------------------------------------------------------------------

def addOperation(pos):
    global equation
    answer=0
        
    firstNumber=float(equation[0:pos])
    print("FIRST NUMBER:",firstNumber)
    
    secondNumber=float(equation[pos+1:len(equation)])
    print("SECOND NUMBER:",secondNumber)

    answer=firstNumber+secondNumber
    displayScreenAnswer(format(answer,'.2f'))
    print('answer:',answer)
    convertToString(answer)

def subtractOperation(pos):
    global equation
    answer=0

    firstNumber=float(equation[0:pos])
    print("FIRST NUMBER:",firstNumber)
    
    secondNumber=float(equation[pos+1:len(equation)])
    print("SECOND NUMBER:",secondNumber)

    answer=firstNumber-secondNumber
    displayScreenAnswer(format(answer,'.2f'))
    print('answer:',answer)
    convertToString(answer)

def multiplyOperation(pos):
    global equation
    answer=0

    firstNumber=float(equation[0:pos])
    print("FIRST NUMBER:",firstNumber)
    
    secondNumber=float(equation[pos+1:len(equation)])
    print("SECOND NUMBER:",secondNumber)

    answer=firstNumber*secondNumber
    displayScreenAnswer(format(answer,'.2f'))
    print('answer:',answer)
    equation=str(answer)

def divideOperation(pos):
    global equation
    answer=0

    firstNumber=float(equation[0:pos])
    print("FIRST NUMBER:",firstNumber)
    
    secondNumber=float(equation[pos+1:len(equation)])
    print("SECOND NUMBER:",secondNumber)

    answer=firstNumber/secondNumber
    displayScreenAnswer(format(answer,'.2f'))
    print('answer:',answer)
    equation=str(answer)

#-------------------------------------------------------------------------------------------------
#FUNCTIONS FOR THE NUMBERS
def one():
    print("1")
    global equation
    equation+='1'
    print(equation)
    displayScreen()

def two():
    print("2")
    global equation
    equation+='2'
    print(equation)
    displayScreen()
    
def three():
    print("3")
    global equation
    equation+="3"
    print(equation)
    displayScreen()

def four():
    print("4")
    global equation
    equation+="4"
    print(equation)
    displayScreen()

def five():
    print("5")
    global equation
    equation+="5"
    print(equation)
    displayScreen()

def six():
    print("6")
    global equation
    equation+="6"
    print(equation)
    displayScreen()

def seven():
    print("7")
    global equation
    equation+="7"
    print(equation)
    displayScreen()

def eight():
    print("8")
    global equation
    equation+="8"
    print(equation)
    displayScreen()

def nine():
    print("9")
    global equation
    equation+="9"
    print(equation)
    displayScreen()

def zero():
    print("0")
    global equation
    equation+="0"
    print(equation)
    displayScreen()

def dot():
    print(".")
    global equation
    equation+="."
    print(equation)
    displayScreen()
    
#-----------------------------------------------------------------------------------------------
#BASIC MATH FUNCTIONS SIGNS AND COMMANDS
def minusSign():
    print("-")
    global equation
    equation+="-"
    print(equation)
    displayScreen()


def plusSign():
    print("+")
    global equation
    equation+="+"
    print(equation)
    displayScreen()


def multiplySign():
    
    global equation
    equation+="x"
    print(equation)
    displayScreen()


def divideSign():
    print("÷")
    global equation
    equation+="÷"
    print(equation)
    displayScreen()
#-------------------------------------------------------------------------------------------------
#ADVANCED FUNCTIONS SIGNS AND COMMANDS

#Sin Function to display "Angle","sin" on to the screen, and error if the equation is not cleared.
#The word 'sin' is added to the equation
def sin():
    print("sin")
    global equation
    equation+="sin"
    x="Angle: "
    displayScreenTrig(x)
    if  equation[0]=='s':
        displayScreenTrig(x)

    elif len(equation)>=3 and equation[0]!='s':
        displayClearError()
    print(equation)

#Cosine Function to display "Angle" for input from user, and error if the equation is not cleared.
#The word 'cos' is added to the equation
def cos():
    print("cos")
    global equation
    equation+="cos"
    x="Angle: "
    if equation[0]=='c':
        displayScreenTrig(x)

    elif len(equation)>=3 and equation[0]!='c':
        displayClearError()
    print(equation)

#Tangent Function to display "Angle" for input from user, and error if the equation is not cleared.
#The word 'tan' is added to the equation
def tan():
    print("tan")
    global equation
    equation+="tan"
    x="Angle: "
    if equation[0]=='t':
        displayScreenTrig(x)

    elif len(equation)>=3 and equation[0]!='t':
        displayClearError()
    print(equation)
#--------------------------------------------------------------------------------------------------------

#equalSign method repeats a specific number of times depending upon on the length of the equation
def equalSign():
    print("=")
    global equation
    position=0

    for counter in range(0,len(equation)):

        if (equation[counter]!='÷' or equation[counter]!='x' or equation[counter]!='+' or equation[counter]!='-') and (counter+1)==len(equation):
            print("ERROR")
            displayError()

        elif(equation[counter])=='t': #Loop searches for the character 't'
            position=counter+3  #Position is recorded as counter+3 because the string 'tan' contains 3 characters and they should not be a part of the calculation(GIGO)
            tanOperation(position)
            break   #Break statement to break the loop after findind the operation character

        elif(equation[counter])=='c': #Loop searches for the character 'c'
            position=counter+3  #Position is recorded as counter+3 because the string 'cos' contains 3 characters and they should not be a part of the calculation(GIGO)
            cosOperation(position)
            break

        elif(equation[counter])=='s': #Loop searches for the character 's'
            position=counter+3  #Position is recorded as counter+3 because the string 'sin' contains 3 characters and they should not be a part of the calculation(GIGO)
            sinOperation(position)
            break
        
        elif equation[counter]=='+': #Loop searches for the character '+' and records the position to be sent to another function
            
            if equation[counter+1]=='x' or equation[counter+1]=='÷':  #Checks if character after the operation symbol is another operation. Displays an error if true.(GIGO)
                displayError()      
                break
            else:
                position=counter
                addOperation(position)
                break
            
            
        elif equation[counter]=='-' and counter!=0: #Loop searches for the character '-' and records the position to be sent to another function
            
            if equation[counter+1]=='x' or equation[counter+1]=='÷':  #Checks if character after the operation symbol is another operation. Displays an error if true.(GIGO)
                displayError()
                break
            else:
                position=counter
                subtractOperation(position)
                break
            
        elif equation[counter]=='x': #Loop searches for the character 'x' and records the position to be sent to another function
            if equation[counter+1]=='x' or equation[counter+1]=='÷':  #Checks if character after the operation symbol is another operation. Displays an error if true.(GIGO)
                displayError()
                break
            else:
                position=counter
                multiplyOperation(position)
                break
            
        elif equation[counter]=='÷': #Loop searches for the character '÷' and records the position to be sent to another function
            if equation[counter+1]=='x' or equation[counter+1]=='÷': #Checks if character after the operation symbol is another operation. Displays an error if true.(GIGO)
                displayError()
                break
            else:
                position=counter
                divideOperation(position)
                break

#-------------------------------------------------------------------------------------------------
#CONVERSION AND OTHER METHODS

#ConvertToString method converts the float converted equation back into string for further inputs(usage)
def convertToString(ans):
    global equation
    ans=float(ans)
    ans=format(ans,'.4f')
    equation=str(ans)

#ExitApp Method: The main window is closed. Before
def exitApp():
    message=tk.messagebox.askquestion('Exit Application','Are you sure you want to quit?')
    if message=='yes':
        mainWindow.destroy()
    else:
        tk.messagebox.showinfo('Return','you will now return')

#-------------------------------------------------------------------------------------------------
#ERROR FUNCTIONS

#Displays an error message when an operation is not entered       
def displayError():
    message=tk.messagebox.showerror('ERROR 404','ERROR')
    
#Diplays an error message when the numbers are not cleared before using the trignometric functions
def displayClearError():
    message=tk.messagebox.showerror('ERROR 404','Clear the numbers before using trignometric functions')
    
#-------------------------------------------------------------------------------------------------
#Clear Function: Clears the equation and displays a blank screen
def clear():
        
    global equation
    equation=''         #The equation string is cleared
    labelOutput=tk.Label(mainWindow, text=equation,
                     fg='yellow',
                     bg='blue',
                     font="Arial 14 bold")
    labelOutput.place(x=25,y=25,width=350,height=75)
    displayScreen()  #Calls the displayScreen function, as the equation doesn't contain anything
#-------------------------------------------------------------------------------------------------
#WINDOW CREATION

#Width and height of the calculator window
width=400
height=700
#Creates the main window
mainWindow=tk.Tk()  
mainWindow.title("Shreyas' Calculator")
mainWindow.minsize(width,height)

#A label that is displayed for the calculations
#screen when the buttons are not yet pressed
labelOutput=tk.Label(mainWindow, text='',
                     fg='yellow',
                     bg='midnight blue',
                     font="Arial 14 bold")
labelOutput.place(x=25,y=25,width=350,height=75)

#A label that displays the title
labelName=tk.Label(mainWindow, text='SCalculator',
                   fg='black',
                   font='Arial 10 italic bold')
labelName.place(x=16, y=10,width=100,height=15)
#------------------------------------------------------------------------------------------------
#BUTTONS CREATION

#Clear Button
buttonClear=tk.Button(mainWindow, text="CLR", fg='red',bg='medium blue', font='Arial 15 bold', command= clear)
buttonClear.place(x=225, y=600, width=50, height=50)

#Button1
buttonOne=tk.Button(mainWindow,text='1', font="Arial 18 bold", command =one)
buttonOne.place(x=25,y=500,width=50,height=50)

#Buuton2
buttonTwo=tk.Button(mainWindow,text='2',font="Arial 18 bold", command=two)
buttonTwo.place(x=125,y=500,width=50,height=50)

#Button3
buttonThree=tk.Button(mainWindow,text='3',font="Arial 18 bold", command=three)
buttonThree.place(x=225,y=500,width=50,height=50)

#Button which displays 4
buttonFour=tk.Button(mainWindow,text='4',font="Arial 18 bold", command=four)
buttonFour.place(x=25,y=400,width=50,height=50)

#Button which displays 5
buttonFive=tk.Button(mainWindow,text='5',font="Arial 18 bold", command=five)
buttonFive.place(x=125,y=400,width=50,height=50)

#Button which displays 6
buttonSix=tk.Button(mainWindow,text='6',font="Arial 18 bold", command=six)
buttonSix.place(x=225,y=400,width=50,height=50)

#Button which displays 7
buttonSeven=tk.Button(mainWindow,text='7',font="Arial 22 bold", command=seven)
buttonSeven.place(x=25,y=300,width=50,height=50)

#Button which displays 8
buttonEight=tk.Button(mainWindow,text='8',font="Arial 18 bold", command=eight)
buttonEight.place(x=125,y=300,width=50,height=50)

#Button which displays 9
buttonNine=tk.Button(mainWindow,text='9',font="Arial 18 bold", command=nine)
buttonNine.place(x=225,y=300,width=50,height=50)

#Button which displays 0
buttonZero=tk.Button(mainWindow,text="0",font="Arial 18 bold",command=zero)
buttonZero.place(x=125,y=600,width=50,height=50)

#Button which displays a decimal Point
buttonDot=tk.Button(mainWindow,text=".",font="Arial 28 bold",command=dot)
buttonDot.place(x=25,y=600,width=50,height=50)

#Button which displays equal to sign
buttonEqualSign=tk.Button(mainWindow,text="=",fg='yellow',bg='black',font="Arial 18 bold",command=equalSign)
buttonEqualSign.place(x=325,y=600,width=50,height=50)

#Button which displays the addition sign
buttonPlusSign=tk.Button(mainWindow,text="+",fg='yellow',bg='black',font="Arial 18 bold",command=plusSign)
buttonPlusSign.place(x=325,y=500,width=50,height=50)

#Button which displays the subtraction sign
buttonMinusSign=tk.Button(mainWindow,text="-",fg='yellow',bg='black',font="Arial 18 bold",command=minusSign)
buttonMinusSign.place(x=325,y=400,width=50,height=50)

#Exit button, when pressed displays a messagebox with 'yes' and 'no'
buttonExit=tk.Button(mainWindow,text='x',fg='black',bg='red',font='Arial 12 bold',command=exitApp)
buttonExit.place(x=380, y=7,width=15,height=15)

#Button which displays Multiplaction sign
buttonMultiplySign=tk.Button(mainWindow,text="x",fg='yellow',bg='black',font="Arial 18 bold",command=multiplySign)
buttonMultiplySign.place(x=325,y=300,width=50,height=50)

#Button which displays the divide sign
buttonDivideSign=tk.Button(mainWindow,text="÷",fg='yellow',bg='black',font="Arial 20",command=divideSign)
buttonDivideSign.place(x=325,y=200,width=50,height=50)

#Button which displays the trignometric 'sin' sign
buttonSin=tk.Button(mainWindow,text="sin",fg='yellow',bg='black',font="Inconsolata 18 bold",command=sin)
buttonSin.place(x=225,y=200,width=50,height=50)

#Button which displays the trignometric 'cosine' sign
buttonCos=tk.Button(mainWindow,text="cos",fg='yellow',bg='black',font="Arial 18 bold",command=cos)
buttonCos.place(x=125,y=200,width=50,height=50)

#Button which displays the trignometric 'tangent' sign
buttonTan=tk.Button(mainWindow,text="tan",fg='yellow',bg='black',font="Arial 18 bold",command=tan)
buttonTan.place(x=25,y=200,width=50,height=50)

#----------------------------------------------------------------------------------------------------------
###################                             END OF PROGRAM                             ################ 
