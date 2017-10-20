fw = open('simple.txt', 'w')
fw.write("Writing ?? on simple text.")
fw.write("This is another fw.write()")
fw.close()

fr = open('simple.txt', 'r')
text = fr.read()
print(text)
fr.close()