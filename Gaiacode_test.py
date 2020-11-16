import math
from math import pi
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
import csv

N = 10
lat_a, lat_b, lat_hex, newlat_hex = [], [], [], []

fig = plt.figure(figsize=(4,4), dpi=150)
ax = fig.add_subplot(111)

def draw_hex(c1, c2, color):
    r = 1 / math.sqrt(3)
    vx, vy = [], []
    for i in range(6):
        a = c1 + r*math.cos(pi/3*i + pi/2)
        b = c2 + r*math.sin(pi/3*i + pi/2)
        vx.append(a)
        vy.append(b)
    vx.append(vx[0])
    vy.append(vy[0])
    line = Line2D(vx, vy, lw=1, c=color)
    ax.add_line(line)

for y in range(N//2):
    for x in range(N):
        lx = float(x)
        ly = (math.sqrt(3) * y)
        #ly = (math.sqrt(3) * y)-math.sqrt(3)
        lyh = math.sqrt(3) * (y+1/2)
        #lyh = math.sqrt(3) * (y+1/2-N/4)
        lat_a.append([lx, ly])
        lat_b.append([lx+1/2, lyh])
        #plt.scatter(lx, ly, s=1, c='k')
        #plt.scatter(lx+1/2, lyh, s=1, c='g')
        #draw_hex(lat_a[-1][0], lat_a[-1][1], 'k')
        #draw_hex(lat_b[-1][0], lat_b[-1][1], 'g')

C_RAD = 3
C_POS = lat_b[25]

for i in range(N**2//2):
    if (lat_a[i][0]-C_POS[0])**2 + (lat_a[i][1]-C_POS[1])**2 <= C_RAD**2:
        lat_hex.append(lat_a[i])
    if (lat_b[i][0]-C_POS[0])**2 + (lat_b[i][1]-C_POS[1])**2 <= C_RAD**2:
        lat_hex.append(lat_b[i])
for i in range(len(lat_hex)):
    newlat_hex.append([lat_hex[i][0]*225, lat_hex[i][1]*225])
for i in newlat_hex:
    plt.scatter(*i, s=1, c='r')
    draw_hex(*i, 'r')
   
print(newlat_hex)
print(type(newlat_hex))

with open(r"beamlocation\37beam.csv",'w')as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(newlat_hex)
    

#C = patches.Circle(xy=C_POS, radius=C_RAD, fill=False)
#ax.add_patch(C)

E_POS = N/2-1
plt.xlim(C_POS[0]-E_POS), (C_POS[0]+E_POS)
plt.ylim(C_POS[1]-E_POS), (C_POS[1]+E_POS)
plt.show()

print(f'Number of beam: {len(lat_hex)}')
