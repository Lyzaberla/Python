#dictionaries is a sspecial structure in python that allows us to 
# store information in key value pairs
#NB: you can use strings, numbers ... etc to store the values

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Aug"]) #this prints out the full name
#another way of getting the stored value
print(month_conversions.get("Jan"))
#in cases where the value you are calling does
# not exist, the printout becomes NONE
print(month_conversions.get("mon")) 


