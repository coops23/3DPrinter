import serial
import timeit
import time


port = 9;
ser = serial.Serial()
ser.port = port - 1
ser.baudrate = 115200
ser.open()
time.sleep(2);

if ser.isOpen == False:
    print "error connecting to arduino"
    sys.exit()
    
start = timeit.timeit()
ser.write("G0 X100\n")
while(ser.readline() != "OK"):
    print "not yet!"

end = timeit.timeit()
seconds = end - start
print str(seconds) + " seconds"

ser.close()
