#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class my_server(Node):
    def __init__(self):
        super().__init__("Server_a_node")
        self.create_service(AddTwoInts,"safe_server",self.srv_call)
        self.get_logger().info("Server start")

    def srv_call(self,rq,rsp):
        req_a=rq.a
        req_b=rq.b
        rsp.sum=req_a+req_b
        self.get_logger().info(str(rsp.sum))
        return rsp


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()