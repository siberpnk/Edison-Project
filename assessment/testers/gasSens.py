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
