import serial
import time 

serialcom = serial.Serial('/dev/ttyUSB0','9600')
serialcom.timeout=1   #wait second close after second 

while True :
    input_user = input ("Enter input")
    if input_user == "Done":
        print("Finish")
        break
    serialcom.write(input_user.encode())
    time.sleep(.5)
    print(serialcom.readline().decode('ascii'))
serialcom.close()