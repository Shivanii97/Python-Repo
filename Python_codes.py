#How to add a new line after the text or how to insert a new line text?
    #Use Escape Sequence Character
    #\n use backslash n, you will get a new line for your txt

    
print("My name is Shivani\nand my age is 25")
     #Ex- My name is Shivani
         #and my age is 25

print("Hi, what are you doing\nand what are your plans for the weekend")
    #Ex- Hi, what are you doing
        #and what are your plans for the weekend

#Double quote escape sequence characters:
# if you want to write the txt in "-" in a string
#we will use backslash double quote; \"-\"
    #Ex: print("Hello World, my name is \"Shivani"\ and I am learning python")

print("Hello World, my name is \"shivani\"\nand my age is 25")
    #Ex- Hello World, my name is "shivani"
         #and my age is 25



#Create a calculator performing addition, substraction,multiplication,divison on two numbers.
a = 50
b = 3

print("The value of" ,a, "+" ,b, " is :", a + b)   # output = The value of 50 + 3 is: 53
print("The value of" ,a, "-" ,b, " is:", a - b)
print("The value of" ,a, "*" ,b, " is:", a * b)
print("The value of" ,a, "/" ,b, " is:", a / b)
print("The value of" ,a, "//" ,b, " is:", a // b)

a = 18
b = 2

print("The value of" ,a, "+" ,b, "is:", a + b)
print("The value of" ,a, "-" ,b, "is:", a + b)
print("The value of" ,a, "*" ,b, "is:", a + b)
print("The value of" ,a, "/" ,b, "is:", a + b)
print("The value of" ,a, "//" ,b, "is:", a + b)

#Typecasting
a = 5
b = 3
print(int(a) + (b))    #output = 8
print(int(a) - (b))
print(int(a) * (b))
print(int(a) /(b))

#Taking user Input
a = input("Enter your Name:")  #Enter your Name:shivani
print("My name is", a)         #My name is shivani

x = input("Enter Your First number:")   #Enter Your First number:10
y = input("Enter Your Second number:")  #Enter Your Second number:5
print(x + y)                            #105 (it will join the numbers, take it as as string)
print(int(x) + int(y))                  #15  ( by using int function, it will add the numbers)

#Create a calculator performing addition, substraction,multiplication,divison on two numbers by using
 #user input method and int() function.

x = input("Enter your first number:")
y = input("Enter your second number:")
print(int(x) + int(y))
print(int(x) - int(y))
print(int(x) / int(y))
print(int(x) * int(y))
print(int(x) // int(y))

#Strings
#Anything that enclose between single or double quotation marks is known as string
name = "Harry"
print("Hello" , name)  #Hello Harry
#Indexing - 0,1,2,3,4,5...etc
print(name[0])  #H [] square brackets is used 

#String Slicing - Lenght of a string, by using len(). To know the length of  string
name = "Today is Monday, and it's sunny"   #output = 13(length of the string)
print(len(name))
print(name[0:7])   #for slicing use[]..output = i(means 0 to 7, the letter is i is comes)
