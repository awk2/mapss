import secrets
import string
import sys

# parse the command line arguments if no argument are specified 
# mapss use the default pattern to create a password 
nm_args = len(sys.argv)
# list of all characters supposed to be used in password
characters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

def usage():
    print("usage: python mapss <pattern>")
    print("<pattern> : l for letters , s for symbols and n for numbers")
    print("example : python mapss lllsslnlslnns")
    quit()

if   nm_args == 2 :
    pattern = [*sys.argv[1]]
elif nm_args == 1 :
    pattern = ['l', 'l', 's', 'l', 'l', 'n', 'n' ,'l', 'l', 'l', 's', 'l']    
else :
    usage()

# create random lists of characters for password using
def create(PassType):
    if PassType == 0:
        randomCharacters=[]	
        for a in range(30):
	        randomizeIndex = secrets.choice(range(len(characters)))
	        randomedCharacter= characters[randomizeIndex]
	        randomCharacters.append(randomedCharacter)
        return randomCharacters
    if PassType == 1:
    	randomNumbers = []
    	for a in range(20):
    		randomNumbers.append(numbers[secrets.choice(range(len(numbers)))])
    	return randomNumbers
    if PassType == 2:
    	randomSymbols = []
    	for a in range(10):
    		randomSymbols.append(symbols[secrets.choice(range(len(symbols)))])
    	return randomSymbols

#loop through the pattern and randomly again choose characters from previous lists 
def validatePattern():
    passwordCharacters = []
    for character in pattern :
        if character =="s":
            passwordCharacters.append(random_punctuation[secrets.choice(range(len(random_punctuation)))])
        if character =="n":
            passwordCharacters.append(random_numbers[secrets.choice(range(len(random_numbers)))])
        if character =="l":
            passwordCharacters.append(random_letters[secrets.choice(range(len(random_letters)))])
    password = "".join(passwordCharacters)
    return password

# init
random_letters     = create(0)
random_numbers     = create(1)
random_punctuation = create(2)

password = validatePattern()
print(password)
