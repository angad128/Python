# Make a funtion that, give a string , return a string.
# return string followed by "!" ,if string is less than 5 charactors. Otherwise , 
# first four characters of string, followed by a "."


def  abberviator(my_string):
	if len(my_string) < 5:
		return str(my_string)+"!"
	else:
		return str(my_string[:4])+"."

print(abberviator("Lion"))
print(abberviator("KINgs"))