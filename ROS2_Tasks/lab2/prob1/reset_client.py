#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.srv import SetBool

class my_server(Node):
    val = 0
    c = False
    state ="None"
    def __init__(self):
        super().__init__("Reset_Client_a_node")
        self.get_logger().info("Reset_Client start ")
        self.service_client(True)

    def service_client(self,a):
        client=self.create_client(SetBool,"reset_server")
        while client.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")
        request=SetBool.Request()
        request.data=a
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)
 
    def future_call(self,future_msg):
        self.get_logger().info("done!")
        


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()