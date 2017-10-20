class Mario:
    def move(self):
        print("I'm moving!")

class Mushroom():
    def eat_mushroom(self):
        print("Now I'm big!")

#multiple Inheritance
class BigMario(Mario,Mushroom):
    pass

bm = BigMario()
bm.move()
bm.eat_mushroom()