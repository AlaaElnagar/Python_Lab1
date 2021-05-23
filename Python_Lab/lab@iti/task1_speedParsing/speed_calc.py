
import math
speed_file= open("python_test_file.txt", "r")

speed_new_file = open("speed_calc.txt", "a")
MainFileData = speed_file.read()
MainFileData = MainFileData.split('\n')
#print (MainFileData)


for val in MainFileData:
    speed_new_file.write(val)
    val = val.split(',')
    if len(val) >16:
        if val[16] != "        ":
            av_speed = math.sqrt( (float(val[16])**2) + (float(val[17])**2)+(float (val[18])**2) )
            speed_new_file.write('\n')
            
            speed_new_file.write("speed = {}".format (str (av_speed)))
            speed_new_file.write('\n')
    else :
        speed_new_file.write('\n')
        speed_new_file.write("speed = 0")
        speed_new_file.write('\n')

    

speed_new_file.close()