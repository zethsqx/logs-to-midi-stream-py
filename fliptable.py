import time
import random

level=1
walker = "(,°.°),"
space = "                                    "
table = "┬─┬"
xVal=-1
yVal=0
zVal=0
pause=0
corridor=""

while True:
  stepdelay=random.randrange(1,5)/10
  time.sleep(stepdelay)    
  if xVal == -37:
    walker = "(╯°□°)╯"
  elif xVal == -38:
    table = "︵┻━┻"
    pause = 1
  xVal +=-1
  corridor = space[xVal:] + walker[xVal:] + space[:xVal] + table
  print(corridor, end="\r")
  if pause == 1:
    time.sleep(2)
    print("............................LEVEL {} RAGE FLIP COMPLETED....................................".format(level))
    level=level+1
  if "(╯°□°)╯︵┻━┻" in corridor:
    walker = "(,°.°),"
    space = "                                    "
    table = "┬─┬"
    xVal=-1
    yVal=0
    zVal=0
    pause=0
    corridor = walker + space + table
    print(corridor)
