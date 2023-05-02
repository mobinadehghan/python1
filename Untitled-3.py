name = input("enter your full name : ")
a = float(int(input("enter your score : ")))
b = float(int(input("enter your score : ")))
c = float(int(input("enter your score : ")))
average = ( a + b + c )/3
if average >= 17 :
    print("statuse : great")

if 12<= average < 17 :
    print("statuse : normal")

if average < 12 :
    print("statuse : fail")