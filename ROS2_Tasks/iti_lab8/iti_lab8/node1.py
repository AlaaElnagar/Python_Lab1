#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String




class my_node(Node):
    flag = 0 
    def __init__(self):
        super().__init__("pub_node")

        self.create_timer(1,self.timer_call)
        self.obj_pub=self.create_publisher(String,"AlaaTopic",10)

        self.get_logger().info("pub_node is started")

    def timer_call(self):
      #  self.get_logger().info("Hello")  # Call Back
        msg1 = String()
        if self.flag == 1 :
            self.flag = 0
            msg1.data="Hi"
        elif self.flag == 0: 
            msg1.data="Hello"
            self.flag = 1
        self.obj_pub.publish(msg1)
      


def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
