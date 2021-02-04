import secrets
import string


#list of all characters supposed to be used in password

characters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# this pattern can be changed depending on the type of password or length
"""
l for letters
n for numbers
s for symbols (punctuation)
"""

pattern="l l l l l l l n n n s n"

# create random lists of characters for password using
def create(PassType):
    if PassType == "word":
        randomCharacters=[]	
        for a in range(30):
	        randomizeIndex = secrets.choice(range(len(characters)))
	        randomedCharacter= characters[randomizeIndex]
	        randomCharacters.append(randomedCharacter)
        return randomCharacters
    if PassType =="numbers":
    	randomNumbers = []
    	for a in range(20):
    		randomNumbers.append(numbers[secrets.choice(range(len(numbers)))])
    	return randomNumbers
    if PassType =="symbole" :
    	randomSymbols = []
    	for a in range(10):
    		randomSymbols.append(symbols[secrets.choice(range(len(symbols)))])
    	return randomSymbols
random_letters = create("word")
random_numbers= create("numbers")
random_punctuation =create("symbole")

#loop through the pattern and randomly again choose characters from previous lists 

def validatePattern():
    pattern_split = pattern.split(" ")
    passwordCharacters = []
    for character in pattern_split :
        if character =="s":
            passwordCharacters.append(random_punctuation[secrets.choice(range(len(random_punctuation)))])
        if character =="n":
            passwordCharacters.append(random_numbers[secrets.choice(range(len(random_numbers)))])
        if character =="l":
            passwordCharacters.append(random_letters[secrets.choice(range(len(random_letters)))])
    password= "".join(passwordCharacters)
    return password
password = validatePattern()
print(password)
