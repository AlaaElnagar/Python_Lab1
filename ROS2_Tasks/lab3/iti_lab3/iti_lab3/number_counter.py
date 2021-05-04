#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
#from example_interfaces.srv import SetBool
from lab_msg_srv.srv import Reset
from lab_msg_srv.msg import  Strint

class my_node(Node):
    val=0

    def __init__(self):
        super().__init__("number_counter")
        self.activated_ = False
        self.sub_sub=self.create_subscription(Strint,"number",self.func_call,10)
        self.obj_pub=self.create_publisher(Strint,"number_counter",10)
        self.get_logger().info("pub_node is started")
        self.create_service(Reset,"reset_server",self.srv_call)

    def func_call (self,msg):
        self.val+=int(msg.num)
        msg2 = Strint()
        msg2.num = self.val
        msg2.data = "{}  {}".format( msg.data, msg.num) 
        self.obj_pub.publish(msg2)
       # self.service_client( self.val, self.val)
       # self.get_logger().info("{} is publishing {}".format( msg.data, msg2.num))
    def srv_call(self, request, response):
        self.activated_ = request.data
        response.result = "Reset---"
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
