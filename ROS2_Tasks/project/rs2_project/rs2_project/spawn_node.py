#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ros2projsrv.srv import Boolsrv
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
import random

class my_node(Node):
    flag = 0
    x_turt_c =0.
    y_turt_c =0.
    theta_turt_c=0.
    def __init__(self):
        super().__init__("spawn_node")

        self.get_logger().info("spawn node is started")
        self.create_service(Boolsrv,"my_server",self.srv_call)




    
    def srv_call(self, request, response):
        if request.arrivedornot:

            client=self.create_client(Kill,"/kill")
            while client.wait_for_service(1)==False:
                self.get_logger().warn("wating for turtlesim")
            req_kill = Kill.Request()
            req_kill.name="AlaaTurtles"
            futur_obj2=client.call_async(req_kill)
            self.flag =1
           
        
        elif request.newturtle  :       
            x_turt=float (random.uniform(1, 10))   
            y_turt=float (random.uniform(1, 10))
            theta_turt=float(random.uniform(0,1.57))
            client=self.create_client(Spawn,"/spawn")
            while client.wait_for_service(1)==False:
                self.get_logger().warn("wating for turtlesim")
            req_spawn =Spawn.Request()
            self.x_turt_c=req_spawn.x= x_turt
            self.y_turt_c=req_spawn.y = y_turt
            self.theta_turt_c=req_spawn.theta = theta_turt
            req_spawn.name ="AlaaTurtles"
            futur_obj=client.call_async(req_spawn)
        response.linrx=self.x_turt_c
        response.linry=self.y_turt_c
        response.linrz=0.

        response.angx = 0.
        response.angy = 0.
        response.angz = self.theta_turt_c


    
            #self.obj_pub.publish(str(self.val))

        return response

def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()


