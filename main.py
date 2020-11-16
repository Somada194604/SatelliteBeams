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

	for deg in range(0, 360, 120):
		x = 2 * r * math.cos(math.radians(deg))
		y = 2 * r * math.sin(math.radians(deg))
		b.addBeam(f1, (x, y))

		x = 2 * r * math.cos(math.radians(deg + 60))
		y = 2 * r * math.sin(math.radians(deg + 60))
		b.addBeam(f2, (x, y))

	for i in range(b.num(f1)):
		#b.plot2d(b.calcCI(f1, i))
		ci = b.calcCI(f1, i)
		print(i, b.calcCIMean(ci, f1, i, r, plot = True))
		#b.plot3dCI(ci)

		ci = b.calcCI(f2, i)
		print(i, b.calcCIMean(ci, f2, i, r, plot = True))
		#b.plot3dCI(ci)
