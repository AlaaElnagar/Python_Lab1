import rclpy
from rclpy.node import Node
from ros2projsrv.srv import Boolsrv
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math



class my_node(Node):
    flag =0
    _err =0.
    _theta =0.
    err_theta =0.

    theta_err = 0.

    main_x= 0.
    main_y= 0.
    main_theta= 0.
    
    sub_x = 0.
    sub_y = 0.
    sub_theta = 0.


    def __init__(self):
        super().__init__("controll_node")
         
        #self.create_timer(1/4,self.timer_call)
        self.sub_sub=self.create_subscription(Pose,"/turtle1/pose",self.func_call,10)
        self.turtle_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("controll_node is started")
        self.serv_client(True,False)
    def func_call(self ,msg):       
        self.main_x =msg.x
        self.main_y = msg.y
        self.main_theta = msg.theta
        self.err_theta = abs(self._theta - self.main_theta )

        if (not (self._err>0 and self._err<1 and self.err_theta <.1 )):
            self.serv_client(False,False)
        else :
             self.serv_client(True,False)
            
       # else :

        

    #def timer_call(self):
      #  self.get_logger().info("Hello")  # Call Back


        
        #self.Turtle_client()
        #self.get_logger().info("check")
        #if self.flag ==0:
        #    self.serv_client(True,False)
        #    self.flag=1 
        #elif self.flag==1:
        #  self.serv_client(False,True)
        #  self.flag =0

        #self.serv_client(True,False)

    def serv_client(self , a,b):
        client=self.create_client(Boolsrv,"my_server")
        
        while client.wait_for_service(1)==False:
            self.get_logger().warn("wating for my_server server")
        request=Boolsrv.Request()
        request.newturtle=a
        request.arrivedornot=b
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)

    def future_call(self,res_msg):
        #self.get_logger().info(str(res_msg.result().state))
        self._err = math.sqrt( pow((self.main_x -res_msg.result().linrx) ,2)+ pow((self.main_y - res_msg.result().linry),2) )
        parallel = abs(self.main_y - res_msg.result().linry)
        adj = abs(self.main_y - res_msg.result().linry)
        if (adj):
            self._theta=math.atan2(parallel,adj)
        self.err_theta = abs(self._theta - self.main_theta )

        T_msg = Twist()
        T_msg._linear.x = 0.                   #self._err
        T_msg._linear.y = 0.
        T_msg._linear.z = 0.


        T_msg.angular.x = 0.
        T_msg.angular.y = 0.
        T_msg.angular.z = self.err_theta

        self.turtle_pub.publish(T_msg)
        if ( self.err_theta <.1):
            T_msg._linear.x = self._err
            T_msg._linear.y = 0.
            T_msg._linear.z = 0.


            T_msg.angular.x = 0.
            T_msg.angular.y = 0.
            T_msg.angular.z = 0.
            self.turtle_pub.publish(T_msg)
        if (self._err>0 and self._err<1 and self.err_theta <.1 ):
            self.serv_client(False,True)
        self.get_logger().info("linx {} -  liny {}".format ( T_msg.angular.y ,T_msg.angular.x ))



def main(args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()
