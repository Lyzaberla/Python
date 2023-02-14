
for letter in "Giraffe Academy":
    print(letter)
#for every letter in Giraffe Academy, print the letter
#this prints out every letter

friends = ["Francis", "Cephas", "Victoria"]
for friend in friends:
    print(friend)
#same as the procedure above

x = [1, 2, 3, 4, 5]
for i in x:
    print(i)
#same as the procedure above

for index in range(10):
    print(index)
#specifying ranges not including the number
for index in range(5, 10):
    print(index)   

friends = ["Francis", "Cephas", "Victoria"]
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
         print("not first")    
