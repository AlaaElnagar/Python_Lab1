#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

from nav_msgs.msg import Path
from geometry_msgs.msg import Pose,PoseStamped

class my_node(Node):
    
    def __init__(self):

        super().__init__("sub_node")
        self.pose_sub=self.create_subscription(Path,"/plan",self.get_robot_pose,10) 

        self.pose_pub=self.create_publisher(Path,"plan_pub",10)

        self.get_logger().info("/plan  subscriper and publisher is started")
#publish lidar data which we get from Bag file  with fresh time stamp
    def get_robot_pose(self,msg):
        points_=Path()
        pose = PoseStamped()

        points_.header.frame_id=msg.header.frame_id
        points_.header.stamp=msg.header.stamp
        #points_.header.seq=msg.header.seq
        pose.pose.position.x = msg.poses.position.x
        pose.pose.position.y = msg.poses.pose.position.y
        pose.pose.position.z = msg.poses.pose.position.z

        pose.pose.orientation.x = msg.poses.pose.orientation.x
        pose.pose.orientation.y = msg.poses.pose.orientation.y
        pose.pose.orientation.z = msg.poses.pose.orientation.z
        pose.pose.orientation.w = msg.poses.pose.orientation.w
        points_.poses.append(pose)

        self.lidar_pub.publish(points_)



        #self.get_logger().info(msg.data)



def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()