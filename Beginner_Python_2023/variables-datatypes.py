#variables are placeholders for data or values
#datatypes are strings(text), numbers(decimal or whole numbers), boolean values
#you need to "quote strings", numbers are fine in plain 12

print("There once was a girl named Elizabeth,")
print("She had the passion for coding,")
print("but didnt know where to start.")
print("Elizabeth mastered the courage and started something,")
print("She started learning how to code consistently at age 23")
print("I am Elizabeth")

print("____________________________________________")
#in the above we have repeated words like Elizabeth
#to make it easier to change the character name or 
#edit anything at all in the story we use variables
print("____________________________________________")
print(" ")

character_name = "Afua"
character_age = "23"
print("There once was a girl named " + character_name +",")
print("She had the passion for coding,")
print("but didnt know where to start.")
print(character_name +" mastered the courage and started something,")
print("She started learning how to code consistently at age " + character_age)
print("I am " + character_name + ".")

print("____________________________________________")
#should you want to change the character name or whatever data 
#you need to alter half way through the story or doc
#then re enter the variable at the said location.
print("____________________________________________")
print(" ")

character_name = "Afua"
character_age = "23"
print("There once was a girl named " + character_name +",")
print("She had the passion for coding,")
print("but didnt know where to start.")

character_name = "Amomea"
print(character_name +" mastered the courage and started something,")
print("She started learning how to code consistently at age " + character_age)
print("I am " + character_name + ".")
