# >>> gerund_infinitive(building)
# return to buind
# >>> gerund_infinitive(swim)
# return That's not gerund

def gerund_infinitive(string):
	if string[-3:] == 'ing':
		return "to " + string[:-3]
	else:
		return "That's not gerund"

print(gerund_infinitive("building"))
print(gerund_infinitive("swim"))
print(gerund_infinitive("swiming"))
print(gerund_infinitive("runing"))
print(gerund_infinitive("look"))