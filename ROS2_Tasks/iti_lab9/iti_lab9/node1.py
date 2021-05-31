#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.msg import Pose
import csv



    

class my_node(Node):
    count = 0
    ext_count=0
    def __init__(self):
        super().__init__("pub_node")

        self.create_timer(1,self.timer_call)
        self.obj_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.sub_sub=self.create_subscription(Pose,"/turtle1/pose",self.func_call,10)
    

        self.get_logger().info("pub_node is started")

    def timer_call(self):
        vel_msg = Twist()
        if  self.ext_count<10:
            self.ext_count+=1
        else :
             self.get_logger().info("Repeate Reading ..")
             self.ext_count = 1

        with open('turtle_commands.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if self.count == self.ext_count :
                    vel_msg.linear.x=float (row[0] )
                    vel_msg.angular.z=float (row[1] )
                 
                   # print(row[0])
                   # print(row[1])
            
                self.count+=1
            self.count = 0
            self.obj_pub.publish(vel_msg)
      #  self.get_logger().info("Hello")  # Call Back

    def func_call (self,msg):

        if (msg.x > 8 or msg.x < 2 or msg.y < 2 or msg.y >8 ):
            client=self.create_client(Empty,"/reset")
            while client.wait_for_service(1)==False:
                self.get_logger().warn("wating for server")
            request=Empty.Request()
            futur_obj=client.call_async(request)
            #self.count = 0
            #self.ext_count=0
        







def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()    


