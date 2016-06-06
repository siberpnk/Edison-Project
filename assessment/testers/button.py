#program for testing button on GPIO port 2(D2)
#by Nikolai Kojevnikov

import mraa, time
button = mraa.Gpio(2);
button.dir(mraa.DIR_IN);
button.read();
x=0;
while True:
    if button.read() == 1:
        x=x+1;
        print x;
