
#include <iostream>
using namespace std ;
#include "task1.hpp"



int main (){
  int n = 0;
while (1){
  cout <<endl<<"--------------------------------------------"<<endl;
  cout <<"Select question between 1 and 7" <<endl ;
  cin >> n ;
  if (n == 1 )
Favourit_num() ;
else if  (n == 2 )
  Reverse_Int();
else if  (n == 3 )
  Access_Array_by_Pointer();
else if  (n ==  4)
  Display_ArrayMaxElement ();
else if  (n == 5 )
  Display_ArrayAverageElement ();
else if  (n == 6 )
  call_add_Class ();
else if  (n == 7 )
  call_Complex_Data();
}

}
