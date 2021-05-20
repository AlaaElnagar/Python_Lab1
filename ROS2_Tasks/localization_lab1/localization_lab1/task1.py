#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np

class my_node(Node):
    count=5
    def __init__(self):
        super().__init__("task1")

        self.sub_sub=self.create_subscription(Imu,"/imu",self.func_call,10)

        self.get_logger().info("Imu sub  is started")
    
    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw 


    def func_call(self):
      #  self.get_logger().info("Hello")  # Call Back
        Imu_msg = Imu()
        #convert into euler rad/sec
        roll,pitch,yaw=self.euler_from_quaternion(self, Imu_msg.orientation) 
        #convert into degree
        yaw*=180/pi
        if (yaw >-2 and yaw <2 ):
            self.get_logger().warn("The robot is nearly heading north .. Heading is: {} degrees".format(yaw) )
        if abs(Imu_msg.linear_acceleration.x) >.3 :
            self.get_logger().warn("Warning !! .. linear acceleration x exceeded the limit . Current acceleration is {} m/s^2 ".format(Imu_msg.linear_acceleration.x) )
        if abs( Imu_msg.angular_velocity.z > .3) :
            self.get_logger().warn("Warning !! .. angular velocity z exceeded the limit . Current Angular velocity is {} rad/sec ".format(Imu_msg.angular_velocity.z) )
         





def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
