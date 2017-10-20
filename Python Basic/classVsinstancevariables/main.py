class Boys:
    #gender is class variable
    gender = "Male"

    def __init__(self, name):
        #name is instance variable
        self.name = name
        print(self.name + " - " + self.gender)

b = Boys('black')
n = Boys('nirajan')
print(b.gender)
print(n.name)
