#include "chrono" //cpp timer lib
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
//#include <iostream>
#include <string>
using namespace  std;


class Node1 : public rclcpp::Node 
 {
public :
    Node1():Node("Node1")
    {
        /*create publisher*/
        string_publisher_ = this ->create_publisher<std_msgs::msg::String>("str_topic",rclcpp::SensorDataQoS()); 
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&Node1::timer_cb, this));

    }
private :
    int count  =0 ;
    void timer_cb (){
        count+=1 ;
        std_msgs::msg::String string_msg = std_msgs::msg::String();
        string_msg.data = "AlaaElnagar,"+to_string(count) ;
        string_publisher_->publish(string_msg); // publishe the message 
        RCLCPP_INFO(this -> get_logger(),string_msg.data);
    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;   // create publisher
    rclcpp::TimerBase::SharedPtr timer_;
 };

int main (int argc, char * argv[]){

    rclcpp::init(argc,argv);     //intialize ros with main arg
    rclcpp::spin(std::make_shared<Node1>());  //call the calss
    rclcpp::shutdown();
    return 0 ;

 }






