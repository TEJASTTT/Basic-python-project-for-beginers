def greet():
    print("Hello sir I am mathician bot How may I help you")

greet()

_1 = str (input("Hello sir so pls ask some mathmatical questions for me if you want to pls type ok in the terminal\n"))

if _1 == ("ok"):
    _4 = str(input("Ok sir now choose the operation out of : +, /, -, *"))
else:
    print("ok sir no problem we will meet again")
    
def addition():
   if _4 ==("+"):
       _2 = float(input("Ok sir so pls tell me the first number"))
       _3 = float(input("Ok sir now tell me the second number"))
   if _4 == ("+"):
        print("Sir the sum of these two numbers are", float(_2) + float(_3))
   else:
        return 0

if _1 ==("ok"):
    if _4 == ("+"):
        addition()

def multiplication():
    if _4 ==("*"):
        _5 = float(input("Ok sir so tell me the first number"))
        _6 = float(input("Ok sir so now tell me the second number"))
    if _4 == ("*"):
        print("Sir the sum of these two numbers are ", float(_5) * float(_6))       
    else:
        return 0
if _1 ==("ok"):
    if _4 == ("*"):
        multiplication()

def division():
    if _4 == ("/"):
        _7 = float(input("Ok sir so tell me the first number"))
        _8 = float(input("Sir now tell me the second number"))
    if _4 == ("/"):
        print("The quotient of these two numbers are", float(_7) / float(_8))
    else:
        return 0

if _1 == ("ok"):
    if _4 == ("/"):
        division()
    
def substraction():
    if _4 ==("-"):
        _9 = float(input("Ok sir so now tell me the first number"))
        _10 = float(input("Ok sir now tell me the second number"))
    if _4 == ("-"):
        print("The difference of these two numbers are", float(_9) - float(_10))

if _1 == ("ok"):
    if _4 == ("-"):
        substraction()
