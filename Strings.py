#Strings
#Anything that enclose between single or double quotation marks is known as string
name = "Harry"
print("Hello" , name)  #Hello Harry

#Indexing - 0,1,2,3,4,5...etc
print(name[0])  #H [] square brackets is used 


name = "Shivani"     
print(name[0])        #S
print(name[1])        #h
print(name[2])        #i

#Looping through the string
#for character in name :
#print(charcter)

apple = ("Hello, how are you, what's going on, what are your plans")
for character in apple :
    print(character)


#String Slicing - Lenght of a string, by using len(). To know the length of  string
name = "Today is Monday, and it's sunny"   #output = 13(length of the string)
print(len(name))
print(name[0:7])   #for slicing use[]..output = i(means 0 to 7, the letter is i is comes)