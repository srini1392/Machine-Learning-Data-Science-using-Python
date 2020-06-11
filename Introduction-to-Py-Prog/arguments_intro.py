'''
Arguments -> default
             keyword
             infinite/flexible number of arguments
'''

def print_something(name ="Marie", age= "unknown"):
    print("my name is", name,"and my age is", age)

print_something("Nick",27)
print_something()
print_something(age=27, name = "Guru")



def print_people(*people):
    for person in people:
        print("this person is ", person)


print_people("Nick","hella","maria","dan", "jack")



def do_math(num1,num2):
    return (num1+num2)

math1 = do_math(5,7)
math2 = do_math(11,34)

print("the first sum is ", math1, "and the second sum is ", math2)

