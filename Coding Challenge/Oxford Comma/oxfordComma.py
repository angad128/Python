l1 = ["Apple","Ball","Cat"]
l2 = ["tiger","lion","bears"]

def comafy(list):
	list[-1] = "and " + list[-1]
	return ',' .join(list)

print(comafy(l1))
print(comafy(l2))