#include "chrono" //cpp timer lib
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <string>
using namespace  std;

class Node2 : public rclcpp::Node 
 {
public :
    Node2():Node("Node2")
    {
        /*create publisher*/
        string_subscriber_ = this->create_subscription<std_msgs::msg::String>("str_topic",10,std::bind(&Node2::timer_cb, this,std::placeholders::_1)); 
        string_publisher_ = this ->create_publisher<std_msgs::msg::String>("int_fb",10); 
    }
private :
    void timer_cb (const std_msgs::msg::String::SharedPtr msg)const{
    
        //int num = stoi( msg->data.c_str()) ;
        string num = msg->data.c_str() ;
        std_msgs::msg::String string_msg = std_msgs::msg::String();
        int flag = 0 ;
        string x = "" ; 
        for (int i = 0 ; num[i] !='\0' ;i++ ){

            if (num[i]==',' || flag ==1 ){
                if (flag ==1){
                     x +=num[i] ; 
                }
                flag = 1 ;
            }


        }
         string_msg.data  = x ;
       // string_msg.data =to_string(num);
       
        RCLCPP_INFO(this -> get_logger(),string_msg.data);
        string_publisher_->publish(string_msg); // publishe the message 

    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr string_subscriber_;   // create publisher
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;   // create publisher

 };

int main (int argc, char * argv[]){

    rclcpp::init(argc,argv);     //intialize ros with main arg
    rclcpp::spin(std::make_shared<Node2>());  //call the calss
    rclcpp::shutdown();
    return 0 ;

 }






