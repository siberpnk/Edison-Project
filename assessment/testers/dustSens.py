#program for testing dust sensor on GPIO port 3(D3)
#by Nikolai Kojevnikov

import mraa, time
dust = mraa.Gpio(3);

class Dust():
    def Ex(self):
        while True:
            self.dustVal=float(dust.read());
            print self.dustVal;
