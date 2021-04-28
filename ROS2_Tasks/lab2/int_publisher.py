#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String



class my_node(Node):
    count=5
    def __init__(self):
        super().__init__("int_publisher")

        self.create_timer(1/2,self.timer_call)
        self.obj_pub=self.create_publisher(String,"number",10)
        self.get_logger().info("int is started")

    def timer_call(self):
      #  self.get_logger().info("Hello")  # Call Back
        msg = String()
        msg.data=str(self.count)
        self.obj_pub.publish(msg)
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
