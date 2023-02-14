
def translate(phrase):
    translation = ""
    vowel = "aeiou"
    for letter in phrase:
        if letter.lower() in vowel:
            if letter.isupper():
                translation = translation + "G"
            else: 
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))



