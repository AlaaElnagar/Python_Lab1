#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class my_node(Node):
    flag = 0

    def __init__(self):
        super().__init__("pub_to_Twist")
        self.create_timer(1,self.timer_call)

        self.obj_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("Pub to Twist start")
    
        self.timer_call ()

    def timer_call (self):
        self.flag +=1 
        #"""Linear x velocity for 1 second """
        if (self.flag ==1):
           # self.create_timer(1,self.flag_inc)
            msg = Twist()
        
            msg.linear.x =  float (1) 
            msg.linear.y =  float (0)
            msg.linear.z =  float (0)

            msg.angular.x = float(0)
            msg.angular.y = float(0)
            msg.angular.z = float(0)

            self.obj_pub.publish(msg)
            self.get_logger().info("Linear x velocity for 1 second")


      # """ Linear x velocity, and angular z velocity for 1 second """
        if (self.flag ==2 ):
           # self.create_timer(1,self.flag_inc)
            msg = Twist()
            msg.linear.x =  float (1) 
            msg.linear.y =  float (0)
            msg.linear.z =  float (0)

            msg.angular.x = float(0)
            msg.angular.y = float(0)
            msg.angular.z = float(1)

            self.obj_pub.publish(msg)
            self.get_logger().info("Linear x velocity, and angular z velocity for 1 second")

        #"""Angular z velocity for 1 second"""
        if (self.flag==3):
           # self.create_timer(1,self.flag_inc)

            msg = Twist()
            msg.linear.x =  float (0) 
            msg.linear.y =  float (0)
            msg.linear.z =  float (0)

            msg.angular.x = float(0)
            msg.angular.y = float(0)
            msg.angular.z = float(1)

            self.obj_pub.publish(msg)
            self.get_logger().info("Angular z velocity for 1 second")

            self.flag = 0
    
    def flag_inc(self):
        self.flag+=1 
       # self.service_client( self.val, self.val)
       # self.get_logger().info("{} is publishing {}".format( msg.data, msg2.num))


def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
