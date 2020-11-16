# -*- coding: utf-8 -*-
from beam.beam2 import Beam
import math

if __name__ == "__main__":
    R = 20
    rep_b = 3 #repetitive beams
    bw = (2.3 * 10 ** 9, 2.5 * 10 ** 9)
    
    f0 = 0
    f1 = 1
    f2 = 2

    b = Beam(R = R, rep_b = rep_b, bw = bw)
    r = b.calcRadius(1000, -2)
    print(r)
    
    b.addBeam(0, (0, 0)) # 0th circle

    for deg in range(30, 360, 60): # 1st circle
        x = 4 * r[f0] * math.cos(math.radians(deg))
        y = 4 * r[f0] * math.sin(math.radians(deg))
        b.addBeam(f0, (x, y))
    
    for deg in range(0, 360, 60):
        dx = r[f1] * math.cos(math.radians(deg))
        dy = r[f1] * math.sin(math.radians(deg))
        
        if deg % 120 == 0:
            b.addBeam(f1, (dx * 2, dy * 2))
        elif deg % 60 == 0:
            b.addBeam(f1, (dx * 4, dy * 4))
    
    for deg in range(60, 361, 60):
        dx = r[f2] * math.cos(math.radians(deg))
        dy = r[f2] * math.sin(math.radians(deg))
        
        if deg % 120 == 0:
            b.addBeam(f2, (dx * 4, dy * 4))
        elif deg % 60 == 0:
            b.addBeam(f2, (dx * 2, dy * 2))

    sum = 0.0
    br = 0.0
    for fn in range(rep_b):
        for i in range(b.num(fn)):
            ci = b.calcCIMean(b.calcCI(fn, i), fn, i, r[fn], plot = True)
            br += b.BitRate(ci)
            sum += ci
            print(i, ci, b.BitRate(ci))
    
    print("average", sum / (b.num(0) + b.num(1) + b.num(2)))
    print("all bitrate", br)
        