#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

from nav_msgs.msg import Path
from geometry_msgs.msg import Pose,PoseStamped

import math





class my_node(Node):
    flag = 0 
    def __init__(self):

        super().__init__("sub_node")
        self.pose_sub=self.create_subscription(Path,"/plan",self.get_robot_pose,10) 

        self.get_logger().info("/plan  subscriper and publisher is started")
        self.string_pub=self.create_publisher(String,"robot_curvature",10)

#publish lidar data which we get from Bag file  with fresh time stamp
    def get_robot_pose(self,msg):
        state =String()
        lenth_ = len(msg.poses)
        curvature=0
        curve_point1_x =0
        curve_point1_y =0

        curve_point2_x = int (lenth_/10)
        curve_point2_y = int (lenth_/10)

        curve_point3_x =int (lenth_/5)
        curve_point3_y =int (lenth_/5)
        #step1  get the lenth of path at first time only 
        if lenth_ >20:
            p1_x=msg.poses[0].pose.position.x
            p1_y=msg.poses[0].pose.position.y

            p2_x=msg.poses[10].pose.position.x
            p2_y=msg.poses[10].pose.position.y

            p3_x=msg.poses[20].pose.position.x
            p3_y=msg.poses[20].pose.position.y
            curvature=self.menger_curvature(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y)

        if curvature>1 :
            state.data=(" The robot is turning with a curvature:{} where {}  is the curavature of the path.".format(curvature , curvature))
            self.get_logger().info("There is a curve  :{}".format(curvature)) 
            self.string_pub.publish(state)
        else :
            state.data=("The path is straight  :{}".format(curvature))
            self.get_logger().info("The path is straight  :{}".format(curvature))
            self.string_pub.publish(state)
       
       
        

    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
            
        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
        return curvature
  



def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
