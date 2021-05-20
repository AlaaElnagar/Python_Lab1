#!/usr/bin/env python3

import rclpy
from rclpy.node import MsgType, Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.msg import Pose
import csv

from sensor_msgs.msg import Imu

from geometry_msgs.msg import Quaternion
from math import sin, cos, pi




class my_node(Node):
    count = 0
    ext_count=0
    def __init__(self):
        super().__init__("pub_node")

        self.create_timer(1/30,self.timer_call)

        self.obj_pub=self.create_publisher(Imu,"zed2_imu",10)


        self.get_logger().info("pub_node is started")

    def quaternion_from_euler(self, roll, pitch, yaw):
        qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
        qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
        qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
        qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
        return Quaternion(x=qx, y=qy, z=qz, w=qw)


    def timer_call(self):
        Imu_msg = Imu()
        Quat_val = Quaternion
        if  self.ext_count<347:
            self.ext_count+=1
        else :
             self.get_logger().info("Repeate Reading ..")
             self.ext_count = 0

        with open('imu_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:

                #set check_limit

                if self.count == self.ext_count :
                #read acc
                    Imu_msg.linear_acceleration.x=float (row[0] ) *9.80
                    Imu_msg.linear_acceleration.y=float (row[1] ) *9.80
                    Imu_msg.linear_acceleration.z=float (row[2] ) *9.80

                    Imu_msg.linear_acceleration_covariance=[0.001, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0, 0.0, 0.001]
                #read gyro
                    Imu_msg.angular_velocity.x=float (row[3] )
                    Imu_msg.angular_velocity.y=float (row[4] )
                    Imu_msg.angular_velocity.z=float (row[5] )
                    #set covar
                    if  Imu_msg.angular_velocity.z < .3 :
                        Imu_msg.angular_velocity_covariance=[0.001, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0, 0.0, 0.001]    
                    else:
                        Imu_msg.angular_velocity_covariance=[0.001, 0.0, 0.0, 0.0, 0.001, 0.0, 0.0, 0.0,10000000.]    

                #read mag
                    Quat_val =  self.quaternion_from_euler(0,0,float(row[6]) )
                    Imu_msg.orientation.x = Quat_val.x
                    Imu_msg.orientation.y = Quat_val.y
                    Imu_msg.orientation.z = Quat_val.z
                    Imu_msg.orientation.w = Quat_val.w
                    
                    if  Imu_msg.angular_velocity.z < .3 :
                        Imu_msg.orientation_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001] #roll , pitch , yaw 
                    else:
                        Imu_msg.orientation_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.] #roll , pitch , yaw 

            
                    self.obj_pub.publish(Imu_msg) 

                self.count+=1
            self.count = 0
            
            self.get_logger().warn("Imu_msg.linear_acceleration.x = {} , Imu_msg.angular_velocity.z= {}".format(Imu_msg.linear_acceleration.x,Imu_msg.angular_velocity.z))
      #  self.get_logger().info("Hello")  # Call Back

    



def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()    

