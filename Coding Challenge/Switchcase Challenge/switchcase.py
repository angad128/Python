s1 = "HELLO"
s2 = "world"
s3 = "i'M herE TO do SOME fuN."

def switchcase(string):
	new_string = ''
	for letter in string:
		if letter.islower():
			new_string += letter.upper()
		else:
			new_string += letter.lower()
	return new_string


print(switchcase(s1))
print(switchcase(s2))
print(switchcase(s3))