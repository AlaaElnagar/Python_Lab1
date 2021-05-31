#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String



class my_node(Node):
    count = 0
    msg1=String()
    def __init__(self):

        super().__init__("str_publisher")
        self.obj_sub_reset_flag=self.create_subscription(String,"reset_flag",self.func,10)
        self.obj_pub_str_topic=self.create_publisher(String,"str_topic",10)         	 	 
        #self.get_logger().info("sub_node is started")
        self.create_timer(1/2,self.timer_call)  
           	 	
    def timer_call(self):
        if self.msg1.data == str(1):
            self.count = 0
        x=str(self.count)
        msg2 =String()
        msg2.data = 'My name is AlaaElnagar ,{}'.format(x)
       # self.get_logger().info(self.msg1.data)
       # self.get_logger().info(msg2.data)
        self.obj_pub_str_topic.publish (msg2)
        self.count+=1
    def func (self,m):
        self.msg1.data=m.data
   
   
        
def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()

