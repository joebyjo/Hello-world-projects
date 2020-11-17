import math

oper = input("what do you want to do?")

while type(oper) == "<class 'str'>":
    number = int(input("enter number"))
    if oper == "factorial":
        print("factorial of " + str(number) + " is " + str(math.factorial(number)))
    elif oper == oper :
        pass

else:
    input("i do not understand that.type 'help' to get list of commands")
