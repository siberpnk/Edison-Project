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
