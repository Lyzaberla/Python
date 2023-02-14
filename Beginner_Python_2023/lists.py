#creating and accessing lists

family = ["solomon", "Deborah", "Esther", "Elizabeth", "Judith", "Jude"]
print(family) #this prints out everthing in the family var
print(family[3]) #this prints out the 4 value, my name
#NB: indexing starts from 0,1,2...etc

# we can access values from the back with negative values
#indexing from the back starts from -1, -2...etc
print(family[-1])

#to access values from a specific range
print(family[3:]) #this prints out values from index 3 going
print(family[1:6]) #this prints out values from index 1 to 5

#to modify values inside the array
# say I want to change 'solomon' 
family[0] = "passed"
print(family[0]) #the value changes


