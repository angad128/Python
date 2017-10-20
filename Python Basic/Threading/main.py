#multiple things runs at once

import threading

class AngoMessanger(threading.Thread):
    def run(self):
        for  _ in range(100):
            print(threading.currentThread().getName())


x = AngoMessanger(name='Send out Messages!')
y= AngoMessanger(name='receive Message!')
x.start()
y.start()