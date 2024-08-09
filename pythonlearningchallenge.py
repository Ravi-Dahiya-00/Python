# what is hashtag # and why it is used in coding ?????
# hastag is used for commenting the code and it is not executed by the computer.
# this is also used for rembering the code what i am doing and also we can tell to our code partner what we are coding.


#paragraph comment 
#it can be written by using triple single cot 
''''how btngwug bng  n u n vk dvn j   nf  nv  f  v i i'''  #like this 


#don't put any punctuations in the end of the code like full stop,comma,etc.
# print('hello world').,               #like this

#Python Indentation
#Indentation refers to the spaces at the beginning of a code line.

#Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

#Python uses indentation to indicate a block of code.



from builtins import complex, input, int, len, print
from typing import TYPE_CHECKING, SupportsComplex                           #this are inbuilt function in  python  and used for not showing an error.


#for writing any line in the code
#we use print and close bracket and double cot and single cot write our statement
print("hello")
print('hello world')


#it is very sensitive language.
#don't use greater letter in PRINT like this it will show error.
#Print("hello world")               #it is wrong method.



#some special characters used in python name with their use
#character      #name                                       #description

#()             #parentheses                                #used with functions.
# #             #pound sign                                 #used for comments.
# ""           #double quotation marks                     #enclose a string.
# '   '           #single quotation marks                     #enclose a string.
#'''  '''        #triple single quotation marks               #used for multiline comments.



print("welcome to python")
print("python is fun")
print('problem driven')



#for writing any mathematical value in the code
#we use only close bracket while writing mathematical value.
#we don't have to use double cot.
print(5)



#using python to perform mathematical computation.
#print(x+y)                          #for addition
#print(x-y)                          #for subtraction
#print(x*y)                          #for multiplication
#print(x/y)                          #for division

#python can be used  for addition,subtraction,multiplication and division.

#for addition we use + sign in between the two numbers.
print(5 + 6)

x=int(input("enter your first number:"))
y=int(input("enter your second number:"))
print(x+y)


#for substraction we use - sign in between the two numbers.
print(7 - 3)

p=int(input("enter your first number:"))
q=int(input("enter your second number:"))
print(p-q)              

#we should take diiferent variable for different calculation of different numbers.



#for multiplication we use * sign in betwwen the two numbers.
print(34 * 56)
print(p*q)

#we can continue with same variable if want all calculation for the same number.



#for division we use / sign in between the two numbers.
print(32 / 4)
print(p/q)


#compute expression
#computeExpression.py

print((10.5 + 2*3) / (45 - 3.5))

#for writing both line and a no in same line we use comma in between numbers and line.
print('hello world', 7, 5)




#programming style and documentation:

#good programming style and proper documentation make a program easy to read and prevent errors.

#programming style refers to the way in which a program is written and formatted.

#proper documentation refers to the written explanations of the code.
#used in big projects to understand the code.


#few guidlines for writting good programming style and proper documentation.


#1. appropriate comments and comment style:
                                  # must include a summary about the code in beginning and with every major step.



#2. proper spacing:
         # a consistent spacing style makes program clear and easy to read, and it also makes it easier to debug.

# print(3+4*5)                           #wrong style

# print(3 + 4 * 5)                      #good style



#programming errors:
#programming errors can be categorized into three types:


#1.syntax error:
              #most common error in python.
              #syntax error results from errors in code cunstruction, such as mistypimg a statement , incorrect indentation, omitting some necessary punctuation, or using an open parenthesis without a corresponding closing parenthesis.


#print("not used puncuation error)  
'''puncutation error'''

# easy to detect because python tells where they are and caused them.

#example:
'''File "<stdin>", line 1
    print("not used puncuation error)
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>>'''



#2. Run-time error:
'''Runtime errors in Python are instances where a program terminates abnormally during execution,often due to incorrect or invalid operations.These errors occur after the program has been successfully compiled, typically when the code attempts to perform operations that are logically or mathematically invalid.'''




#example
'''Some examples of Python runtime errors:

1. division by zero
2. performing an operation on incompatible types
3. using an identifier which has not been defined
4. accessing a list element, dictionary value or object attribute which doesn’t exist
5. trying to access a file which doesn’t exist'''



#3. logic error:
'''it occures when the program does not perform the way it was intended to.
      errors of this kind occur for a variety of reasons,
      such as incorrect assumptions about the program's behaviour'''

#example:
'''some example of python logic errors:

converting a string to an integer 
using the wrong comprasion operator
using the wrong logical error operator
using the wrong arithmetic operator
using the wrong assignment operator
using the wrong membership operator
using the wrong identity operator
using the wrong bitwise operator
using the wrong ternary operator'''



#convert fahrenhit to celsius:
print("fahrenhit 35 is celsius degree")
print("celsius degree is" ,5/9 * (35-32))       #correct method it will show 1.6667



#but if use wrong operator it will show different answer:
print("fahrenhit 35 is celsius degree")
print("celsius degree is" ,5 / 9 * 35 - 32)        #wrong method it will show -12.55 because we didn't tell which         calculation is to be done first.



#in python, syntax errors are treated as run-time errors because they are detected by the interpreter when the program is executed.


#in general, syntax and runtime errors are easy to find and easy to correct , because python gives indications as to where the error is and ehy they are wrong.


#logic errors finding can be very challenging.



#getting started with graphics programming:
#TURTLE is python's built in graphics module for drawing lines,circles,and other shapes,including text.
#it is easy to learn and simple to use.


#drawing and adding color to a figure:
#1. open python
#2. import turtle
#3. turtle.showturtle()
#4. to draw a string 
         #turtle.write("welcome to python")
#5. to move the arrowhead 100 pixels forward to draw a line in the direction the arrow is pointing:
         #turtle.forward(100)
#6. to turn the arrowhead 90 degrees to the right:
       #turtle.right(90)
#7. to change the turtle's color to red:
       #turtle.color("red")
#8. to move the arrowhead 50 pixels forward to draw a line :
       #turtle.forward(50)
#9. to change the turtle's color to green:
       #turtle.color("green")
#10. to turn the arrowhead 30 degree to the left:
       #turtle.left(30)
#11. you can now close the turtle graphics windows and exit python.

import turtle
turtle.showturtle()
turtle.write("welcome to python")
turtle.forward(100)
turtle.color("red")
turtle.right(90)
turtle.forward(40)
turtle.left(20)
turtle.forward(100)
turtle.right(45)



#moving pen to any location:

     #when the turtle program starts, the arrowhead is at centre of the screen.
     #coordinates of turtle are(0,0)
     #we use goto() function to move the turtle to any location. specified location(x,y)


turtle.goto(0,50)

#to draw a circle:
                #draw a circle using cirlce command.

turtle.circle(50)   #50 is radius of circle.


#to draw a dot:
             #draw a dot using dot command.


turtle.dot(50)


# we can also use penup() and pendown() functions to move the turtle without drawing a line.


#penup() function is used to stop drawing.
#pendown() function is used to start drawing.

turtle.penup()
turtle.goto(50,-50)
turtle.pendown()



                    #made a olympic ring logo using turtle.
                       # file = olympicring.py

#something intersting:
                #if we want something in design and in more than one line we can write it by using some logic.

#let's see:
          #python program to display patterns:


print(" FFFFFFFFFF      UU            UU        NN            NNN ")
print(" FF              UU            UU        NN N          NN  ")
print(" FF              UU            UU        NN   N        NN  ")
print(" FFFFFFFFF       UU            UU        NN     N      NN  ")
print(" FF               UU          UU         NN       N    NN  ")
print(" FF                UU        UU          NN         N  NN  ")
print(" FF                  UUUUUUUU           NNN           NNN  ")

#this was only for fun purpose but it also provided one different logic to think it about.


#we can also create a table using print statement.

print("A Program To Display The Table: ")
print("a", 
             "a^2",
                         "a^3")         #written in different line for spacing in between the characters a, a^2;a^3.
print(1,         1*1,       1*1*1)
print(2,         2*2,       2*2*2)
print(3,         3*3,       3*3*3)
print(4,         4*4,       4*4*4)

print((9.5*4.5-2.5*3)/(45.5-3.5))













#writing a simple program
#writing a program involves designing a strategy for solving the problemand then using a programming language to implement that srategy.



#circlearea.py


#assign a value to radius
radius=20               #radius is now 20

#compue area
area=radius*radius*3.14159

#display results
print("the area of circle of radius",radius,"is",area)

#radius is a variable that has a fix value 20 that is stored in computers memory and can be used anytime when the program needs variable.
#python automatically figures out the data type according to the value assigned to the variable.we need not to specify what types of values are being used.


width=5.5
height=2
print("area is ", width,*height)

miles=100
kilometers=miles*1.609
print("100miles have",kilometers,"kilometers")


#INPUT function is used for taking user input
variableradius=print(input("enter a value"))


#prompt the user to enter a radius
radius=eval(input("enter a value for radius:"))                     #eval converted the string to number


#compute area
area=radius*radius*3.14159


#display results
print("the area for the circle of radius",radius,"is",area)


#reading input from the console
#reading console enables the program to accept input from the user.

s=input("enter a value for radius:")                    #read input as a string
radius=eval(s)                                        #conert the string to a number

#int can also be used for converting the string into a number
x=int(input("enter your first number"))        #if int is not used it will take it is a string



# for starting a new a line and continue the same statement
#but in the next line we use \n
print('hellofriends \nthis is my first code')  #\n for new line

#for using double cot in between the lines we use \''
print('he is a \'good\'boy')
#for coting good in comma we use \'good\'

#for sepreating the words we use sep='~'
#and whatever with which symbol we want to sepreate
print('hello', 5, 6, sep='~')
#wew cannot write something after seperate.
#only we can use ending line after seperate.

#we want to end our code with something
#we use end='line with which we want to end our code'
print(
    6,
    4,
    9,
    sep="~",
    end="thanks",
)
#what is variable and why we use it????
#variable is like a container that holds data.
#creating a variable is like creating a placeholder in memory
# and assigning it some value.
#in python,variable is created the moment you assign a value to it.

#variable holds.
#this is required in programming to do various operation without causing an error.

#types of data type in python
#1. numeric data type
#2. text data type
#3. boolean data type
#4. sequenced data type
#5. mapped data type

#what is numeric data type????
#numeric data type specifies the numeric value like int ,float,complex.

#int:represensts the integer value.
#float:represents the floating value.
#complex:represents the complex value.

#what is data type????
#data type specifies the type of value 

#example of numeric data type
a = 1  #integer data type
b = 2.5  #float data type
c = complex(2, 3)  #complex data type

print('\n', a)  #'\n' is used for new line
print(b)
print(c)

#what is text data type????
#text data type specifies the text value like str,string.

#str:represents the string value.
#string:represents the string value.

#example of text data type
a = 'hello'  #string data type
b = 'world'  #string data type

print(a, '\n', b)

#what is boolean data type????
#boolean data type specifies the next value like true false.

#example of boolean data type
a = True  #boolean data type     #T should be capital
b = False  #boolean data type     #F should be capital

print(a)
print(b)
print(a, b)

#what is sequenced data type?    ???
#sequenced data type specifies the next value like list,tuple.

#list represents the list value.
#tuple represents the tuple value.

#example of sequenced data type.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(a)

list1 = [8, 2.3, [-4, 5], ['apple', 'banana']]
print(
    list1
)  #list is a collection of different data types.it can be changed these are mutable.

tuple1 = (('parrot', 'sparrow'))

print(tuple1)
#tuple is a collection of different data types.it can be changed these are immutable.

#what is mapped data type????
#mapped data type specifies the next value like dict,dict.

#dict represents the dict value.
#dict represents the dict value.

#exaple of mapped data type.
a = {'name': 'Ravi', 'age': '17', 'canvote': 'true'}

print(a)

print(2 + 8)  #addition of two numbers. +
print(9 - 5)  #substraction of two numbers. -
print(5 * 3)  #multiplication of two numbers. *
print(5 / 3)  #division of two numbers. /
print(
    7 // 2
)  #floor division of two numbers. //    used to calculate approx division of two numbers.
print(
    5 % 3
)  #modulus of two numbers. %    used to calculate reminder of two numbers.
print(
    5**3
)  #exponential of two numbers. **    used to calculate power of two numbers.

#type casting in python
#the conversion of one data type into the another data type is known as type casting in python or type conversion in python.

#python supports a wide variety of functions or method like: int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict(),etc for the type casting in python.

#two types of type casting in python:
#1.explicit conversion
#2.implicit conversion

# what is explicit type casting????
#the conversion of one data type into another data type,done via developer or programmer`s intervention or manually as per the requirment,is known as explicit type casting.

#example of explicit type casting
a = "1"
b = "2"
print(
    a + b
)  #it will not add the numbers because these are string and these are printed in a line.
print(
    int(a) + int(b)
)  # A and B are string and these are converted into ineger by using int() function.

#what is implicit type casting????
#data types in python do not have the same level i.e. ordering of data types is not the same in python.
#some of the data types have higher order and some have lower order.while performing any operation on varibles with different data types in python ,
#one of the variable data types will be changed to the higher data type.
#according to the level,one data type is converted into other by the python interpreter itself(automatically) in the background.
#this is called implicit type casting in python.

#example of implicit type casting
a = 1.9
b = 8
print(a + b)

string = "15"
number = 7
string_number = int(
    string)  #throws an error if the string is not a valid integer
sum = number + string_number
print("the sum of both the numbers is:", sum)

#user input in python
#in python,we can take user input directly by using input() function.
#this input function gives a return value as string/character hence we have to pass that int() to the function.

#example of user input
a = input('enter your name:')
print("my name is",a)
X=input("enter first number:")
Y=input("enter second number:")

print((X)+(Y))

print(int(X)+int(Y))


#what are string in python????
#in python, anything that you enclose between single and double quotation marks is considered as string.
#a string is essentially a sequence or array of textual data.
#strings are used when working with unicodes characters.


#example of string
name="ravi"
friend="rohan"
anotherfriend="lovish"

x=input("enter friend name:")

print("hello"+name)

print("your friend is " + x)
#talk="he said "he wants to eat an apple""

#this line will show an error because we cannot use double cot in double cot.


#1st
#method to resolve this error
#so we use escape sequence character.

talk="he said \"he wants to eat an apple\""

print(talk)


#2nd 
#method to resove this same error
#so we can enclose our string in single cot.

talk='he said "he wants to eat an apple"'

print(talk)


#3rd
#method to resolvis same error
#so we can use single triple cot.

talk='''he said "he wants to eat an apple"'''

print(talk)


#4th
#method to resolvis same error
#so we can use double triple cot.
talk="""he said "he wants to eat an apple" """

print(talk)


#basically we use triple cot for multiline string.
#this help in copy and paste the string.

apple='''hi ravi
how are you doing
i am good
call me later '''

print(apple)

#this is main use of triple single cot.
#we can also use triple double cot for this purpose.


#indexing in python
#in python,string is like an array of characters.(array=collection of items)
#we can access parts of string by using its index which starts from 0.
#square brackets can be used to access elements of the string.


#example of indexing
name="ravi"
print(name[0])
print(name[1])
print(name[2])
print(name[3])


#print(name[4]) 
#throws an error because index 4 doesnot exist in this name.

#looping through the string
#we can loop through string using a for loop like this:
#example of looping through the string

print("lets use a for loop\n")

name="ravi"

for character in name:
    print(character)


#slicing string and operation on string
#what is string slicing????
#length of a string can be found using len() function.
#we can find the length of a string using len() function.

#example of string slicing
name="ravi"
print(len(name))

#counting in python starts from 0 not from 1 .


fruit="mango"
len1=len(fruit)
print("mango is a ",len1,"letter word.")

#string as an array
#a string is essentially a sequence of characters also called an array.
#thus we can access the elements of this array.
#example of string as an array
pie="applepie"
print(pie[0:5])  #this will print the first 5 letters of the string.
#including 0 but not 5.



print(pie[:5])    # it is not neccesary to write 0 in the starting.
#python automattically adds 0 in the starting.


print (pie[1:5])   #it will not print the 0th letter that is A .
#it  will print the first letter that is P.
#including 1 but not 5.


print(pie[6])    #this will only print the 6th letter of the string.



#negative slicing in python
#we can also use negative slicing in python.
#it is similar to positive slicing.
#but the counting in negative slicing starts from the end and -1 is added in the ending.



#example of negative slicing
pie="applepie"


print(pie[0:-3]) #it will subtract the 3 letters from the end of the string.

#python will consider it like this:
print(pie[0:len(pie)-3])


# both the  above things are same and have same output.


#when we will change sign of both the numbers.

print(pie[-1:-3])   

#python will consider it like this:
#6:3
#there is no sense in this.
#so python will not print anything.



#if if interchange the numbers.

print(pie[-3:-1])
#python will consider it like this:
#3:6
#so python will print the letters from 3 to 6.
#but it will not print the 6th letter that is E because
#it is not included because of the negative slicing.

nm="harry"
print(nm[-4:-2])

#if it is positive slicing or negative slicing 
#python will print the first number written but not the second number written.
#it uses n-1 for writting the second number.


#strings are immutable
#a string in python cannot be changed.
#but strings can be replaced by new strings.
#it can be done by using string methods.


#string methods in python:
#python provides a set of built-in methods that we can use to alter and modify the strings.

#there are various types of string methods in python.
#they are as follows:

#1.   upper()
#2.   lower()
#3.   strip()
#4.   rstrip()
#5.   lstrip()
#6.   replace()
#7.   split()
#8.   capitalize()
#9.   center()
#10.   count()
#11.  ends with()
#12.  find()
#13.  index()
#14.  isalnum()
#15.  isalpha()
#16.  islower()
#17.  isprintable()
#18.  isspace()
#19.  istitle()
#20.  isupper()
#21.  startswith()
#22.  swapcase()
#23.  title()


#example of string methods


#1.   upper()
a="Ravi"
print(a.upper())    #it will print the string in upper case.


#2.   lower()
a="Ravi"
print(a.lower())     # it will print the string in lower case.


#3.   strip()
a="Ravi!!!!!!!"
print(a.strip("!"))    #it will remove the trailing characters.
# it will not remove the leading characters.
#it removes spaces,tabs,new lines,carrige returns,vertical tabs and form feed characters.
a="Ravi@@@"
print(a.strip("@"))  


#4.   rstrip()
a="!!Ravi!!!!!"
print(a.rstrip("!"))  #it will remove the trailing characters from right side of string.


#5.   lstrip()
a="!!!Ravi!!!!!"
print(a.lstrip("!"))    #it will remove the leading characters from left side of string.


#6.   replace()
a="Ravi"
print(a.replace("Ravi","rao"))   #it will replace the string with another string.


#7.   split()
#the split() method splits the given string at the specified instance and returns the separated string as list items.


a="Ravi-is a good boy"
print(a.split("-"))   #it will split the string into a list.
#it will split the string from the given character we have given between the split().



#8.   capitalize()
#the capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
#the string has no effect if the first character is already uppercase.
#it also changes middle of the string if uppercase then it will change to lowercase.


blogheading="inTroDuctIon to PythOn"
print(blogheading.capitalize())



#9.   center()
#the centre() method aligns the string to the center as per the parameters given by the user.

str1="welcome to the console!!!"
print(str1.center(50))

print(len(str1))
print(len(str1.center(50)))

#why we put 50 in bracket of center() function???
#because we want to write in mid of the screen and to find the mid of the screen we can use len() function and use double the number of len() in center().
#it will give mid of the screen.


      
#10.   count()
#the count() method returns the number of times the given value has occured within the given string.

a= "ravi is a good boy.ravi plays cricket."
print(a.count("ravi"))

#we can count number of word is used and letter also.


#11.   ends with()
#the ends with() method checks if the string ends with a given value.
#if yes then return true,else return false.
a="@Ravi!!!!"
print(a.endswith("@"))  #it will return false.
print(a.endswith("!!!"))  #it will return true. 



#we can also check for a value in between the string by providing start and end index positions.
a=" welcome to the console!!!"
print(a.endswith("to",4,10))  #it will return true.
#it will check whether the string ends with to between 4 and 10.

print(a.startswith("@"),a.endswith("!!!"))



#12.   find()
#the find() methods searches for the first occurence of the given value and returns the index where it is present.
#if given value is absent from the string then return -1.


a="he's name is dan.he is an honest man."


print(a.find("is"))   #gives the index of first occurence of the give value.

print(a.find("ishh"))   #gives -1 because ishh is not present in the string.


#13.   index()
#the index() method searches for the first occurence of the given value and returns the index where it is present.
#if given value is absent from the string then raise an exception.


a="he's name is dan.he is an honest man."
print(a.index("dan"))    #gives the index of first occurence of the give value.

#print(a.index("ishh"))
      #gives an error because ishh is not present in the string.



#14.   isalnum()
#the isalnum() method returns true only if the entire string only consists of A-Z,a-z,0-9.
#if any other character or punctuations are present,then it returns false.


str1="WelcomeToTheConsole123"
print(str1.isalnum())   #it will return true.

str2="Welcome!!!!!!!!!!"
print(str2.isalnum())    #it will return false.



#15.   isalpha()
#the isalpha() method returns true only if the entire string only consists of A-Z,a-z.
#if any other character or punctuations or numbers(0-9) are present,then it returns false.


str1="welcome"
print(str1.isalpha())   #it will reurn true.

str2="welcome123"
print(str2.isalpha())    #it will return false.


#16.   islower()
#the islower() method returns true if all the characters in the string are lower case.
#else it returns false.


str1="hello world"      #it will return true.
print(str1.islower())


str2="Hello World"
print(str2.islower())   #it will return false



#17.   isprintable()
#the isprintable() method returns true if all the values within the given string are printable.
#if not,then return false.

str1="we wish you a merry christmas"
print(str1.isprintable())   #it will return true.


str2="we wish you a merry christmas\n"  #i.e \n is not printable.
print(str2.isprintable())   #it will return false.


#18.   isspace()
#the isspace() method returns true only and only if the string contains white spaces.
#else returns false.

str1="hello world"
print(str1.isspace())   #it will return false.


str2="   "
print(str2.isspace())    #it will return true.


#19.   istitle()
#the istitle() method returns true only if the first letter of each word of the string is capitalized.
#else it reurns false.


str1="World Health Organaization"
print(str1.istitle())   #it will return true.


str2="to kill a Mocking bird"
print(str2.istitle())   #it will return false.



#20.   isupper()
#the isupper() method returns true if all the characters in the string are upper case.
#else it returns false.


str1="WORLD HEALTH ORGANIZATION"
print(str1.isupper())   #it will return true.


str2="WORLD HEALTH organization"  #it will return false.
print(str2.isupper())



#21.   startswith()
#the startswith() method checks if the string starts with a given value.
#if yes then return true,else return false.


str1="python is a interpreted language"
print(str1.startswith("python"))  #it will return true.

print(str1.startswith("hello"))    #it will return false.




#22.   swapcase()
#the swapcase() method changes the character casing of the string.
#upper case are converted to lower case and lowercase are converted to upper case.

str1="HELLO friends ThIs iS a PYTHON program"
print(str1.swapcase())



#23.   title()
#the title() method capitalizes each letter of the word within the string.

str1="hello friends this is a PYTHON PROGRAM"
print(str1.title())



# if else conditional statements


    #sometimes the programmer needs to check the evaluation of certain expression(s).
#whether the expression evaluates to true or false.
#if the expression evaluates to false,then the program execution follows a different path then it would have if the expression evaluates to true.

#conditinal opeartors

# > , < , >= , <= , == , !=
# print(a>18)   #it is true only when a is greater then 18.
# print(a<=18)   #it is true only when a is less than or equal to 18.
# print(a==18) # it is true only when a  is equal to 18.
# print(a!=18)  #







