# Make a function that, give a Nepal
# 14 zones abbreviation, returns the zone's name.

zones = {"ME": "Mechi","KO":"Koshi","SA":"Sagarmatha","JA":"Janakpur","BA":"Bagmati","NA":"Narayani","LU":"Lumbini","GA":"Gandaki","NA":"Narayani","RA":"Rapti","VE":"Veri","KA":"Karnali","SE":"Seti","MA":"Mahakali"}

def look_zones(abbreviation):
	return zones[abbreviation] 

print(look_zones("BA"))
print(look_zones("SA"))