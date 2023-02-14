#working with list functions
age = [53, 57, 29, 23, 20, 20]
family = ["solomon", "Deborah", "Esther", "Elizabeth", "Jude", "Judith"]
print(age)
print(family)

#to join the two lists
family.extend(age)
print(family) #prints out everything from the age, family joined

#to add to the list
family.append("Dagny") #add to the end of the list
print(family)

#to insert at the middle
family.insert(2, "Elionna") #positions the value at index 2
print(family)

#to remove an element from the list
family.remove("solomon") #it removes solomon from the list
print(family)

#to clear the list 
#family.clear()

#to clear the last element
family.pop()
print(family)

#to find if a value or element is in the list 
print(family.index("Elionna")) #returns the index location of Elionna

#to check for repeated values or similar values
print(family.count(20)) #reuturns the number of times 20 appeared

#to sort the list
#NB: it cannot sort between strings and integers
age.sort()
print(age) #returns sorting in ascending order

#to reverse a list (flip the list)
age.reverse()
print(age)

#to copy a list
age2 = age.copy()
print(age2) #returns a copy of the copied list
