
# Abuya, Brandon J.
# BSCS 1-1
# To do the correction for invalid codes, I made it so that I have an else statement when I am converting parts of the morse code to
# letters that corresponds to when the user inputs a line of morse code that doesnt correspond to any of the letter in the alphabet. I identified
# that there is 4 combination of morse code that doesnt equal to any of the letters which are (---. : ---- : .-.- : ..--). With this info,
# I first concatenate the invalid code to my invalid code text then cut down the invalid code to a maximum of 4 digits only as that is the maximum
# number of digits of valid code. I would then check if this code is equal to any of the invalid codes I identified earlier. If they are, they would
# be corrected to be a similar code that is valid. For example, ---. being corrected to --.. which is only one digit off. If it does not match the 4 invalid
# combination I identified, it means the cutted down code is already valid and I just print that.

end = False
lettercheck = False
invalid = False
i = 0
morsecode = input("Code:")
lmorse = ""
text = ""
invalidcode = ""

while not end:
	if i == len(morsecode):
		lettercheck = True
		end = True
	elif morsecode[i] == '/' or morsecode[i] == '\\': 
		lettercheck = True
	else:
		lmorse += morsecode[i]
		i += 1
	while lettercheck:
		if lmorse == ".-":
			text += 'A'
		elif lmorse == "-...":
			text += 'B'
		elif lmorse == "-.-.":
			text += 'C'
		elif lmorse == "-..":
			text += 'D'
		elif lmorse == ".":
			text += 'E'
		elif lmorse == "..-.":
			text += 'F'
		elif lmorse == "--.":
			text += 'G'
		elif lmorse == "....":
			text += 'H'
		elif lmorse == "..":
			text += 'I'
		elif lmorse == ".---":
			text += 'J'
		elif lmorse == "-.-":
			text += 'K'
		elif lmorse == ".-..":
			text += 'L'
		elif lmorse == "--":
			text += 'M'
		elif lmorse == "-.":
			text += 'N'
		elif lmorse == "---":
			text += 'O'
		elif lmorse == ".--.":
			text += 'P'
		elif lmorse == "--.-":
			text += 'Q'
		elif lmorse == ".-.":
			text += 'R'
		elif lmorse == "...":
			text += 'S'
		elif lmorse == "-":
			text += 'T'
		elif lmorse == "..-":
			text += 'U'
		elif lmorse == "...-":
			text += 'V'
		elif lmorse == ".--":
			text += 'W'
		elif lmorse == "-..-":
			text += 'X'
		elif lmorse == "-.--":
			text += 'Y'
		elif lmorse == "--..":
			text += 'Z'
		else:
			invalidcode += lmorse 
			lmorse = lmorse[0:4]
			if lmorse == "---.":
				invalidcode += " : Try --.. instead."
			elif lmorse == "----":
				invalidcode += " : Try -.-- instead."
			elif lmorse == ".-.-":
				invalidcode += " : Try .--- instead."
			elif lmorse == "..--":
				invalidcode += " : Try ...- instead."
			elif lmorse == "":
				invalidcode += "Empty code detected"
				invalidcode += " : Try .... instead."
			else:
				invalidcode += " : Try " + lmorse + " instead."
			if i < len(morsecode):
				invalidcode += "\n"
			invalid = True
	
		if i < len(morsecode):
			if morsecode[i] == '/':
				text += ' '
		lmorse = ""
		lettercheck = False
		i += 1

if not invalid:
	print("Text:" + text)
elif invalid:
	print("Invalid. The following codes cannot be translated:\n" + invalidcode)
	
	
	