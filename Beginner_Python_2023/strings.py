#strings are text
print("Elizabeth is taking a course from giraffe academy.")

print("____________________________________________")
print(" ")
#to enter a new line we use \n
print("Elizabeth \nis taking a course from giraffe academy")

print("____________________________________________")
print(" ")
#to printout a quotation mark use \ then " so \"
print("Elizabeth \nis taking a course from \"giraffe academy\"")

print("____________________________________________")
print(" ")
#to printout the back slash just insert it
print("Elizabeth is taking a course \ from giraffe academy")

print("____________________________________________")
print(" ")
#to store the string in a string variable
sentence = "Elizabeth is taking a course from giraffe academy."
print(sentence)
 #for concatination
print(sentence + "to be a master")

print("____________________________________________")
print(" ")
#for the use of functions .function
print(sentence.lower())
print(sentence.capitalize())
print(sentence.upper())
#for checking if the string function is true or false
print(sentence.isupper())
#for running the functions together
#it runs the first two then the next
print(sentence.upper().isupper())
#to check length of string
print(len(sentence))
#to get the first character of the string (ARRAY)
print(sentence[0])
print(sentence[1])
print(sentence[2])
#to find where a letter is located on the index 
print(sentence.index("g"))
#to replace a text or anything
print(sentence.replace("Elizabeth","Afua"))



