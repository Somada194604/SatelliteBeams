# -*- coding: utf-8 -*-
from beam.beam import Beam
import math

if __name__ == "__main__":
    f1 = 2.5 * 10 ** 9
    f2 = 2.675 * 10 ** 9
    f3 = 2.85 * 10 ** 9
    r = 112.5 # -3[dB] radius

    b = Beam()
    l1 = b.addFreq(f1)
    l2 = b.addFreq(f2)
    l3 = b.addFreq(f3)
    
    b.addBeam(f1, (0, 0)) # 0th circle
    
    for deg in range(60, 361, 60):
        dx = r * math.cos(math.radians(deg))
        dy = r * math.sin(math.radians(deg))
        
        if deg % 120 == 0:
            b.addBeam(f2, (dx * 2, dy * 2))
        elif deg % 60 == 0:
            b.addBeam(f1, (dx * 2, dy * 2))
            
    for deg in range(30, 361, 30): # 1st circle
        dx = r * math.cos(math.radians(deg))
        dy = r * math.sin(math.radians(deg))
        
        if deg % 60 == 0:
            b.addBeam(f2, (dx * 4, dy * 4))        

        elif deg % 30 == 0:
            b.addBeam(f1, (dx * 4, dy * 4))

    sum = 0.0
    for fn in [f1, f2]:
        for i in range(b.num(fn)):
            ci = b.calcCIMean(b.calcCI(fn, i), fn, i, r, plot = True)
            sum += ci
            print(i, ci)
            print(i,b.BitRate(ci))
    
    print("average", sum / (b.num(f1) + b.num(f2)))
    
        