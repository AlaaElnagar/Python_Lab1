from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
	ob=LaunchDescription()
	n1=Node(
		package ='iti_lab3',
		executable ='int_pub')
	
	n2=Node(
		package ='iti_lab3',
		executable ='number_count')

	ob.add_action(n1)
	ob.add_action(n2)
	return ob
	
	
