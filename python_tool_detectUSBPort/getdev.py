
# info = os.popen('dir').read() #read dir elements 

import os

os.system ("ls /dev > USB_devices.txt")
DevFile= open("USB_devices.txt", "r")

Dev_Name = input ("Enter your USB port name:")
File_Data = DevFile.read()
File_Data = File_Data.split()
flag = 0 
for Dev in File_Data :
    if Dev == Dev_Name:
        print("Your device exist ")
        flag=1
if flag == 0 :
    print("Your device Isn't connected ")

# os.system ("python -m serial.tools.list_ports > USB_devices.txt")
# print(DevFile.read())
# print(File_Data)
