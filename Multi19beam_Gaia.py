# -*- coding: utf-8 -*-
from beam.beam import Beam
import math
from math import pi
#import matplotlib.pyplot as plt
#import matplotlib.patches as patches
#from matplotlib.lines import Line2D


if __name__ == "__main__":
    N = 8
    f1 = 2.5 * 10 ** 9
    f2 = 2.675 * 10 ** 9
    f3 = 2.85 * 10 ** 9
    r = 112.5 # -3[dB] radius

    b = Beam()
    l1 = b.addFreq(f1)
    l2 = b.addFreq(f2)
    l3 = b.addFreq(f3)
    lat_a, lat_b, lat_hex, newlat_hex = [], [], [], []
    
    #b.addBeam(f1, (0, 0)) # 0th circle
    
    for y in range(N//2):
        for x in range(N):
            lx = float(x)
            ly = math.sqrt(3) * y
            lyh = math.sqrt(3) * (y+1/2)
            lat_a.append([lx, ly])
            lat_b.append([lx+1/2, lyh])
#            plt.scatter(lx, ly, s=1, c='k')
#            plt.scatter(lx+1/2, lyh, s=1, c='g')
#            draw_hex(lat_a[-1][0], lat_a[-1][1], 'k')
#            draw_hex(lat_b[-1][0], lat_b[-1][1], 'g')

    C_RAD = 2
    C_POS = lat_b[10]

    for i in range(N**2//2):
        if (lat_a[i][0]-C_POS[0])**2 + (lat_a[i][1]-C_POS[1])**2 <= C_RAD**2:
            lat_hex.append(lat_a[i])
            if (lat_b[i][0]-C_POS[0])**2 + (lat_b[i][1]-C_POS[1])**2 <= C_RAD**2:
                lat_hex.append(lat_b[i])
    for i in range(len(lat_hex)):
        newlat_hex.append([lat_hex[i][0]*r, lat_hex[i][1]*r])
        b.addBeam(f1, (lat_hex[i][0]*r, lat_hex[i][1]*r))
                #for i in lat_hex:
                    #plt.scatter(*i, s=1, c='r')
                    #draw_hex(*i, 'r')

    #C = patches.Circle(xy=C_POS, radius=C_RAD, fill=False)
    #ax.add_patch(C)

    E_POS = N/2-1
    #plt.xlim(C_POS[0]-E_POS, C_POS[0]+E_POS)
    #plt.ylim(C_POS[1]-E_POS, C_POS[1]+E_POS)
    #plt.show()

    print(f'Number of beam: {len(lat_hex)}')
                    
    sum = 0.0
    for fn in [f1]:
        for i in range(b.num(fn)):
            ci = b.calcCIMean(b.calcCI(fn, i), fn, i, r, plot = True)
            sum += ci
            print(i, ci)
            print(i,b.BitRate(ci))
    
    print("average", sum / (b.num(f1) + b.num(f2) + b.num(f3)))
    
        