#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String



class my_node(Node):
    count=0 	
    msg_reset_flag = String()
    msg_reset_flag.data =str(0)
    def __init__(self):
        super().__init__("number_counter")
    #    self.create_timer(1/2,self.timer_call)
        self.obj_pub_number=self.create_publisher(String,"number",10)
        self.obj_pub_reset_flag=self.create_publisher(String,"reset_flag",10) 	
        self.obj_sub_str_topic=self.create_subscription(String,"str_topic",self.str_topic_recive,10)  
        #self.get_logger().info("number_counter is started")
    def str_topic_recive(self,msg1):   
        msg_number = String()
        msg_str_topic = String()
        x= msg1.data 
        x=x.split(",")
        #self.get_logger().info("the value of x = :{}".format(x[1]))
        if int(x[1])%6 == 0 and int(x[1]) != 0 :
            self.count =0
            self.msg_reset_flag.data = str(1)
        else :
            self.msg_reset_flag.data = str(0)
            self.count = int(x[1])
            msg_number.data=str(self.count)
        self.obj_pub_number.publish(msg_number)
        self.obj_pub_reset_flag.publish(self.msg_reset_flag)
       #self.get_logger().info('reset_flag val = {}'.format(self.msg_reset_flag.data))  # Call Back
       #self.get_logger().info('countr = {}'.format(self.count))  # Call Back



def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

