from launch import LaunchDescription
import launch.actions
import launch_ros.actions


def generate_launch_description():    
    return LaunchDescription([
        
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '1.77', '0', '0', '0', 'base_link', 'gps_link'],
            ),

        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['1.92', '0.36', '0', '0', '0', '0', 'base_link', 'lidar_link'],
            ),
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['1.8', '-.03', '0', '0', '0', '0', 'base_link', 'zed_link'],
            ),
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['-0.10', '0', '0.88', '3.142', '0', '0', 'base_link', 'mynt_link'],   
            ),
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['1.8', '-0.50', '1', '1.57', '0', '0', 'base_link', 'imu_link'],
            ),            
       

    ])
