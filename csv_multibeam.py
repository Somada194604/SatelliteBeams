from beam.beam import Beam
import math
import csv

f1 = 2.5 * 10 ** 9
f2 = 2.675 * 10 ** 9
f3 = 2.85 * 10 ** 9
r = 112.5 # -3[dB] radius

x = []
y = []
freq = []
b = Beam()
l1 = b.addFreq(f1)
l2 = b.addFreq(f2)
l3 = b.addFreq(f3)

with open('C:\\Users\\somad\\OneDrive\\デスクトップ\\専攻科\\特別研究\\SatelliteBeams\\multibeam_37beam.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        freq.append(int(row[0]))
        x.append(float(row[1]))
        y.append(float(row[2]))
        if(freq[-1]==1):
            b.addBeam(f1, (x[-1], y[-1]))
        elif(freq[-1]==2):
            b.addBeam(f2, (x[-1], y[-1]))
        elif(freq[-1]==3):
            b.addBeam(f3, (x[-1], y[-1]))

sum = 0.0
for fn in [f1, f2, f3]:
    for i in range(b.num(fn)):
        ci = b.calcCIMean(b.calcCI(fn, i), fn, i, r, plot = True)
        sum += ci
        print(i+1, ci)
        print(i+1,b.BitRate(ci))
    
print("average", sum / (b.num(f1) + b.num(f2) + b.num(f3)))