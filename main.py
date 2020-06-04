#import numpy as np
import sounddevice as sd
import random
from scipy import *
import music as M, numpy as n

while True:
#  fs = random.randrange(3000, 40000, 2) 
#  data = n.random.uniform(-1, 0, fs)

  sd.play(data, fs, blocking=True)
