#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.srv import SetBool


class my_node(Node):
    val=0

    def __init__(self):
        super().__init__("number_counter")
        self.activated_ = False
        self.sub_sub=self.create_subscription(String,"number",self.func_call,10)
        self.obj_pub=self.create_publisher(String,"number_counter",10)
        self.get_logger().info("pub_node is started")
        self.create_service(SetBool,"reset_server",self.srv_call)

    def func_call (self,msg):
        self.val+=int(msg.data)
        msg2 = String()
        msg2.data = str(self.val)
        self.obj_pub.publish(msg2)
       # self.service_client( self.val, self.val)
        self.get_logger().info(msg2.data)
    def srv_call(self, request, response):
        self.activated_ = request.data
        response.success = True
        if self.activated_:
            self.val = 0
            #self.obj_pub.publish(str(self.val))

        return response

def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
