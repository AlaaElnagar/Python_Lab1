"""               Python Assignments               """

"""
1) Write a python code that ask the user to
enter his birth year and then print his age in
years.
"""
def GetBirhDate() :
    age    = int (input("please enter your age :"))
    birth  = "you are {0} years old "
    print(birth.format(2021-age))

"""
2) Write a python code to find Sum and Average of
N Natural
Numbers
"""
def GetSumAndAverage():
    num = int (input("Enter num to get sum and Average"))
    sum,av=0,0
    for n in range(num+1) :
        print(n)
        sum+=n
    avr=sum/num
    print("The sum of Natural numbers from 1 to {} = {}" .format (num,sum))
    print("The Average of Natural numbers from 1 to {} = {}" .format (num,avr))

"""
3) Pyramid Pattern with Stars
"""

def PyramidOfStars():
    num = int (input("Enter num to get it's  Pyramid shape:"))
    for n in range(1,num+1):
        if (n==1):
            print(((num-n)*" ")+(( (num-(num-n))*"*")))
        else:
            print(((num-n)*" ")+(( (((num-(num-n))*(2))-1)*"*")))

"""
4) Python Program to Check Even or Odd
"""

def EvenOrodd():
    exit_char= "A"
    while exit_char !='q':

        num=(input("Enter q for exit. \nEnter any number: "))
        if (str(num)!='q'):
            if int(num)%2 == 0 :
                print("{}is even number ".format(num))
            else:
                print("{}is odd number ".format(num))
        else:
            exit_char='q'
"""
5) Remove Vowels from String
"""
Vowels_tub = ('a','e','o','i','y')
def RemVowels ():
    exit_char= "A"
    while exit_char !='q':

        StringWithVowels=(str(input("Enter q for exit. \nENTER ANY STRING TO REMOVE ALL VOWELS FROM IT :"))).lower()
        if (StringWithVowels!="q"):
            StringWithOutVowels=""
            vowelFlag=0
            for char in StringWithVowels:
                for vowel in Vowels_tub:
                    if char == vowel:
                        vowelFlag=1

                if vowelFlag==0:
                    StringWithOutVowels+=char
                vowelFlag=0
            print("New string after successfully removed all vowels :{}".format(StringWithOutVowels))
        else:
            exit_char ='q'

"""
6)Write a Python program to write a list to a file.
"""
def WriteListToFile():
    ListElements = str(input("Enter all of list elements separated by space:"))
    ListElements =ListElements.split()
    File = open("Alaa_file.txt",'a+')
    for l in (ListElements):
        File.write(l)
    File.close()

"""
7)Write a Python function to sum all the numbers in a list
"""

def sum (list):
    Total=0;
    for element in list :
        Total+=int(element)
    return(Total)

def call_sum():

    ListElements = str(input("Enter all of list elements separated by space:"))
    ListElements =ListElements.split()
    print(sum(ListElements))

"""
8) Write a Python program to print the even numbers from
a given list.
"""

def EvenNumOFList():

    ListElements = str(input("Enter all of list elements separated by space:"))
    ListElements =ListElements.split()
    List2= list()
    for element in ListElements:
        if int (element)%2 ==0:
            List2.append(element)
    print("[",end='')
    i =0
    for element in List2:
            print(element,end='')
            i+=1
            if i < len(List2):
                print(",",end='')

    print("]",end='')

""""
9)
Write a Python class which has two methods get_String and
print_String . get_String accept a string from the user and print_String
print the string in upper case.

"""
class String:
    S=""
    def get_String(self):
        self.S=str(input ("Enter your string: "))
    def print_String(self):
        print("Your string is :{}".format((self.S).upper()))

def call_String():
    class_mem =String()
    class_mem.get_String()
    print(class_mem.print_String())

"""
10) Write a python class to calculate the average speed, distance travelled and
the trip duration of a vehicle: car, bus, train, bike, motorcycle, plane etc.
constructed by a Distance (Km) and Time(H) and a method which will
compute the speed of a car.
"""

class Speed ():
    def __init__(self,Time_H,Distance_Km):
        self.Time_H=Time_H
        self.Distance_Km=Distance_Km
    def Get_average_Speed(self):
        print("your average speed is :",(self.Distance_Km/self.Time_H))

def call_speed():
    Rocket = Speed(24,5000)
    Rocket.Get_average_Speed()


"""
14) Write a program that repeatedly prompts a user for integer numbers until
the user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it
with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
"""

def GetMaxNum():
    exit_char= "A"
    lis = list()
    max=0

    while exit_char !="done":
        num=input("Enter done to quit/n or Enter a number:")
        if num !="done":
            try:
                num=int(num)
                lis.append(num)
            except:
                print("Invalid input")

        else :
            exit_char="done"
            min =lis[0]
            for num in lis:
                if int(num) > max :
                    max =int(num)
                if int (num) <min:
                    min =int(num)
            print("The maximum num you have enterd is {}".format(max))
            print("The Minimum num you have enterd is {}".format(min))

"""
15) Write a program that prompts for a file name, then opens that file
and reads through the file, and print the contents of the file in upper
case. Use the file words.txt to produce the output below.
"""

def ReadFile():
    FileName = str(input ("enter file name to read:"))
    File = open(FileName,'r')
    for line in File :
        print(line.upper(),end='')



"""
16) Open the file mbox
short.txt and read it line by line. When you find a line that starts with 'From ' like the following line
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person w
ho
sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
"""
def ParseFile():
    File = open("mbox-short.txt",'r')
    text = File.readlines()
    for line in text:
        line=line.split()
        if (len(line)):
            word =line[0]
        if word =="From:":
            for w in range(1,len(line)):
                print(line[w],end='')
            print("")
