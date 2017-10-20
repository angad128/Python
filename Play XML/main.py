import os
import xml.etree.ElementTree as et


base_path = os.path.dirname(os.path.realpath(__file__))
#print(base_path)

xml_file = os.path.join(base_path,"data\productListing.xml")
#print(xml_file)

tree = et.parse(xml_file)

root = tree.getroot()

#for child in root:
#	print(child)
#	print(child.tag)

#for child in root:
#	for element in child:
#		print(element.tag,":",element.text)

new_product = et.SubElement(root,"product",attribute={"id":"4"})
new_product_name = et.SubElement(new_product,"new_product_name")
new_product_desc = et.SubElement(new_product,"description")
new_product_cost = et.SubElement(new_product,"cost")
new_product_ship = et.SubElement(new_product,"shipping")

new_product_name.text = "Python Pants"
new_product_desc.text = "Ne awesome pythom pants!"
new_product_cost.text = "49.99"
new_product_ship.text = "4.00"

tree.write(xml_file)

for child in root:
	for element in child:
		print(element.tag,":",element.text)
