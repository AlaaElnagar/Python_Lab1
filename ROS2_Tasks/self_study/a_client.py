#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from example_interfaces.msg import String

class my_server(Node):
    val = 0
    def __init__(self):
        super().__init__("Client_a_node")
        self.get_logger().info("Client start ")
        self.obj_pub=self.create_subscription(String,"AlaaTopic",self.func_call,10)
        self.get_logger().info("AlasaTopic is started")

        self.service_client( self.val, self.val)
        self.service_client(10,20)
    def func_call (self,msg):
        self.val=int(msg.data)
        self.service_client( self.val, self.val)
        self.get_logger().info(msg.data)
    def service_client(self,a,b):
        client=self.create_client(AddTwoInts,"safe_server")
        while client.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")
        request=AddTwoInts.Request()
        request.a=a
        request.b=b
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)
 
    def future_call(self,future_msg):
        self.get_logger().info(str(future_msg.result().sum))
        


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()