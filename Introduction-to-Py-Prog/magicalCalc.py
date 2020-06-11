import re
print("Our magical calculator")
print("type 'quit' to exit\n")
previous = 0
run = True


def performMath():
    global run #access the global variable
    global previous
    equation = ""

    if previous == 0:
        equation = input("enter the equation: ")
    else:
        equation = input(str(previous))




    if equation == 'quit':
        print("Goodbye, Human")
        run = False
    else :
        equation = re.sub('[a-zA-Z,.:()" "]]', '',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)


while run:
    performMath()
