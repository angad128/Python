Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> players = [1,2,5,7,9,10,18,21,23,30,22]
>>> len(players)
11
>>> players[0]
1
>>> players[:11]
[1, 2, 5, 7, 9, 10, 18, 21, 23, 30, 22]
>>> players[0:11]
[1, 2, 5, 7, 9, 10, 18, 21, 23, 30, 22]
>>> players[0:10]
[1, 2, 5, 7, 9, 10, 18, 21, 23, 30]
>>> players[4] = 99
>>> players
[1, 2, 5, 7, 99, 10, 18, 21, 23, 30, 22]
>>> players + [90.91,92]
[1, 2, 5, 7, 99, 10, 18, 21, 23, 30, 22, 90.91, 92]
>>> players
[1, 2, 5, 7, 99, 10, 18, 21, 23, 30, 22]
>>> players.append([50,51,52])
>>> players
[1, 2, 5, 7, 99, 10, 18, 21, 23, 30, 22, [50, 51, 52]]
>>> players[11]
[50, 51, 52]
>>> players.append(70,71)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    players.append(70,71)
TypeError: append() takes exactly one argument (2 given)
>>> players.append(70)
>>> players
[1, 2, 5, 7, 99, 10, 18, 21, 23, 30, 22, [50, 51, 52], 70]
>>> players[-2]
[50, 51, 52]
>>> players[-2] = 11
>>> players
[1, 2, 5, 7, 99, 10, 18, 21, 23, 30, 22, 11, 70]
>>> players[0:3] = [0,0,0]
>>> players
[0, 0, 0, 7, 99, 10, 18, 21, 23, 30, 22, 11, 70]
>>> players[:2] = []
>>> players
[0, 7, 99, 10, 18, 21, 23, 30, 22, 11, 70]
>>> players = []
>>> players
[]
>>> 
