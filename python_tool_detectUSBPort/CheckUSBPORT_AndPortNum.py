
# info = os.popen('dir').read() #read dir elements 

import os
os.system ("udevadm info -e> USB_devices.txt")
#os.system ("ls /dev > USB_devices.txt")
DevFile= open("USB_devices.txt", "r")

Dev_Name =str( input ("Enter your USB port name:"))
File_Data = DevFile.read()
File_Data = File_Data.split()
# pos = File_Data.find(Dev_Name)
Line_num =0
Line_Identifier = "devices"
Flag = 0;
for i,line in enumerate(File_Data):
    if Dev_Name in line:
        if Line_Identifier in line:
            Line_num = i
            Flag =1
            break
# print(File_Data[Line_num])
if Flag ==1 :        
    mydev_line=File_Data[Line_num]
    mydev_line = mydev_line.split("/")
#     print(mydev_line)

    for i,line in enumerate(mydev_line):
        if "usb" in line:
            Line_num = i
            break
    mydev_line=mydev_line[Line_num]    
#     print(mydev_line)
    print ("Your device exist and its in {}".format(mydev_line))
else :
    print("Can't read your device ")



# print(mydev_line)
# for Dev in File_Data :
#     if Dev == Dev_Name:
#         print("Your device exist ")
#         flag=1
# if flag == 0 :
#     print("Your device Isn't connected ")

# os.system ("python -m serial.tools.list_ports > USB_devices.txt")
# print(DevFile.read())
# print(File_Data)
