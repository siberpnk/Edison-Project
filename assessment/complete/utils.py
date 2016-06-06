#class file for loudness sensor Aio  1(A1)
#by Nikolai Kojevnikov

import mraa, time
loud = mraa.Aio(1);
#gasVal=float(gas.read());

class Loud():

    def Ex(self):
        while True:
            self.loudVal=float(loud.read());
            print self.loudVal;
#program for testing gas sensor on Aio port 0(A0)
#by Nikolai Kojevnikov

import mraa, time
gas = mraa.Aio(0);
#gasVal=float(gas.read());

class Gas():
    def Ex(self):
        while True:
            self.gasVal=float(gas.read());
            print self.gasVal;
#program for testing dust sensor on GPIO port 3(D3)
#by Nikolai Kojevnikov

import mraa, time
dust = mraa.Gpio(3);

class Dust():
    def Ex(self):
        while True:
            self.dustVal=float(dust.read());
            print self.dustVal;
