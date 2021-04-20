from Q1 import *

Escape_char  = "start"

while(Escape_char != "end"):
    Prog_num=int(input("please enter numbre of Question from 1 to 16 "))

    if (Prog_num) == 1 :
        GetBirhDate()
    elif Prog_num == 2 :
        GetSumAndAverage()
    elif Prog_num == 3 :
        PyramidOfStars()
    elif Prog_num == 4 :
        EvenOrodd()
    elif Prog_num == 5 :
        RemVowels ()
    elif Prog_num == 6 :
        WriteListToFile()
    elif Prog_num == 7 :
        call_sum()
    elif Prog_num == 8 :
        EvenNumOFList()
    elif Prog_num == 9 :
        call_String()
    elif Prog_num == 10 :
        call_speed()
    elif Prog_num == 11 :
        matrix_numpy()
    elif Prog_num == 12:
        Remove_Negative()
    elif Prog_num == 13 :
        shift_left()
    elif Prog_num == 14 :
         GetMaxNum()
    elif Prog_num == 15 :
         ReadFile()
    elif Prog_num == 16 :
         ParseFile()
