#coding=utf-8
import sys

def line1(num):

    if(num=='0'):
        return "66666"
    elif(num=='1'):
        return "....6"
    elif(num=='2'):
        return "66666"
    elif(num=='3'):
        return "66666"
    elif(num=='4'):
        return "6...6"
    elif(num=='5'):
        return "66666"
    elif(num=='6'):
        return "66666"
    elif(num=='7'):
        return "66666"
    elif(num=='8'):
        return "66666"
    elif(num=='9'):
        return "66666"

def line2(num):

    if(num=='0'):
        return "6...6"
    elif(num=='1'):
        return "....6"
    elif(num=='2'):
        return "....6"
    elif(num=='3'):
        return "....6"
    elif(num=='4'):
        return "6...6"
    elif(num=='5'):
        return "6...."
    elif(num=='6'):
        return "6...."
    elif(num=='7'):
        return "....6"
    elif(num=='8'):
        return "6...6"
    elif(num=='9'):
        return "6...6"

def line3(num):

    if(num=='0'):
        return "6...6"
    elif(num=='1'):
        return "....6"
    elif(num=='2'):
        return "66666"
    elif(num=='3'):
        return "66666"
    elif(num=='4'):
        return "66666"
    elif(num=='5'):
        return "66666"
    elif(num=='6'):
        return "66666"
    elif(num=='7'):
        return "....6"
    elif(num=='8'):
        return "66666"
    elif(num=='9'):
        return "66666"

def line4(num):

    if(num=='0'):
        return "6...6"
    elif(num=='1'):
        return "....6"
    elif(num=='2'):
        return "6...."
    elif(num=='3'):
        return "....6"
    elif(num=='4'):
        return "....6"
    elif(num=='5'):
        return "....6"
    elif(num=='6'):
        return "6...6"
    elif(num=='7'):
        return "....6"
    elif(num=='8'):
        return "6...6"
    elif(num=='9'):
        return "....6"

def line5(num):

    if(num=='0'):
        return "66666"
    elif(num=='1'):
        return "....6"
    elif(num=='2'):
        return "66666"
    elif(num=='3'):
        return "66666"
    elif(num=='4'):
        return "....6"
    elif(num=='5'):
        return "66666"
    elif(num=='6'):
        return "66666"
    elif(num=='7'):
        return "....6"
    elif(num=='8'):
        return "66666"
    elif(num=='9'):
        return "66666"

def showAndPrint(num):
    res1 = ""
    res2 = ""
    res3 = ""
    res4 = ""
    res5 = ""
    for j in num:
        res1 += line1(j) + ".."
        res2 += line2(j) + ".."
        res3 += line3(j) + ".."
        res4 += line4(j) + ".."
        res5 += line5(j) + ".."

    print(res1[:-2] + '\n' + res2[:-2] + '\n' + res3[:-2] + '\n' + res4[:-2] + '\n' + res5[:-2])


if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())

    for i in range(n):        
        line = sys.stdin.readline().strip()

        showAndPrint(str(eval(line.lstrip().rstrip("="))))