#conditional statements
is_male = False

if is_male:
    print("you are a male")
else: 
    print("you are a female") 

#using the OR operation
is_female = True
is_fair = False

if is_female or is_fair:
    print("You are a woman")
else:
    print("You are a man")    

#using the And operation
is_human = True
is_alive = False

if is_human and is_alive:
    print("Congratulaltions, You are a Living being")
else:
    print("I do not know what You are...")    

#using the else if
is_human = True
is_alive = False

if is_human and is_alive:
    print("Congratulaltions, You are a Living being")
elif is_human and not is_alive:
    print("Welcome")    
else:
    print("I do not know what You are...")    

