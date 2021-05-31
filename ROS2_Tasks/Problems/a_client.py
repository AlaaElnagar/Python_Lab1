#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class my_server(Node):
    def __init__(self):
        super().__init__("Client_a_node")
        user_name = "AlaaELnagar"
        self.service_client(8,9,user_name)
        self.service_client(10,20,user_name)



    def service_client(self,a,b,user_name):
        client=self.create_client(AddTwoInts,"safe_server")
        while client.wait_for_service(.1)==False:
            self.get_logger().warn("wating for server")
        if user_name =="AlaaElnagar":
            request=AddTwoInts.Request()
            request.a=a
            request.b=b
            futur_obj=client.call_async(request)
            futur_obj.add_done_callback(self.future_call)
        else :
            self.get_logger().info(user_name)
            self.get_logger().info("wrong user name ")

    def future_call(self,future_msg):
        self.get_logger().info(str(future_msg.result().sum))
        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()