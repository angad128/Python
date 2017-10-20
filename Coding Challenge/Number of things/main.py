# >>> how_many([5,"Apple"])
# There is 5 Apples.
# >>> how_many([1,"Soul"])
# There is 1 Soul.

def how_many(the_list):
	if the_list[0] == 1:
		return "There is " + str(the_list[0]) + " " + str(the_list[1])+"."
	else:
		return "There is " + str(the_list[0]) + " " +  str(the_list[1])+"s."

print(how_many([5,"Apple"]))
print(how_many([1,"Soul"]))