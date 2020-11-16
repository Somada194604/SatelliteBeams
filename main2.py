from beam.beam import Beam
import math

if __name__ == "__main__":
    f1 = 2.5 * 10 ** 9
    f2 = 2.4 * 10 ** 9
    f3 = 2.3 * 10 ** 9
    r = 112.5 # -3[dB] radius

    b = Beam()
    l1 = b.addFreq(f1)
    l2 = b.addFreq(f2)
    l3 = b.addFreq(f3)

    for deg in range(0, 360, 60):
        dx = r * math.cos(math.radians(deg))
        dy = r * math.sin(math.radians(deg))
        
        if deg % 120 == 0:
            b.addBeam(f1, (dx * 2, dy * 2))
        elif deg % 60 == 0:
            b.addBeam(f1, (dx * 4, dy * 4))
        #b.addBeam(f2, (x, y))

    for i in range(b.num(f1)):
        #b.plot2d(b.calcCI(f1, i))
        ci = b.calcCI(f1, i)
        print(i, b.calcCIMean(ci, f1, i, r, plot = True))
        #b.plot3dCI(ci)

        #ci = b.calcCI(f2, i)
        #print(i, b.calcCIMean(ci, f2, i, r * f1 / f2, plot = True))
        #b.plot3dCI(ci)