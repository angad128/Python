class Parent():
    def print_last_name(self):
        print('Budhathoki')


#single iniheritance
class Child(Parent):
    def print_name(self):
        print('Angad ')

#function overriding and multiple iniritance
class Child2(Child):
    def print_last_name(self):
        print('Budhathoki')

ango= Child()
ango.print_name()
ango.print_last_name()

mango = Child2()
mango.print_name()
mango.print_last_name()