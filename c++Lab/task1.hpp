
/*
Low Speed Self
driving Vehicles ITI
1) Create a C++ program that asks the user for their favorite number
between 1 and 100. Then read this number from the console.
Suppose the user enters number 24 you want to display the
following to the console.
Amazing.
That's my favorite number too.
*/
void Favourit_num(){
  int num =0;
  cout <<"Enter your num between 1 and 100:" ;
  cin  >>num ;
  if (num <= 100 && num >=0){
    cout <<"Amazing!! Thast's my favourte number too!!"<<'\n'<<"No really!! "<<num<<" is my favourite number !"<<endl ;
  }
}

/*
2) Create a C++ program to Reverse an Integer
*/

void Reverse_Int(){
int Integ ;
cout <<"enter integer :" ;
cin>>Integ ;
float f = Integ ;
int num=0;
while (f >1) {
  f=f/10 ;
  num= (f - int(f)) *10 ;
  cout<<num ;
}
cout <<endl ;

}

/*
3) Access Array Elements Using Pointer
*/

void Access_Array_by_Pointer(){

  int array [5] = {0} ;
  int *ptr = array ;
  int n = 0;
  cout <<"Enter elements:";

  for (int i = 0 ; i < 5 ; i ++){

  cin >>n ;
  array [i] = n ;
  }
  cout <<"You enterd :"<<endl ;

  for (int i = 0 ; i < 5 ; i ++){

  cout <<  ptr[i] <<'\n' ;
  }
}

/*
4) Display Largest Element of an array
*/
void Display_ArrayMaxElement ()
{
  int num =0;
  int max = 0;
  int arr[100] ={0} ;
  cout <<"Enter your num of elements between 1 and 100:" ;
  cin  >>num ;
  if (num <= 100 && num >=0){
    int n = 0;
    for ( int i =  0 ; i <num ; i ++){

      cout <<endl<<"Enter num:"<<i <<":";
          cin >>n ;
  max = n ;
    }

    for ( int i =  0 ; i <num ; i ++){

    if (max < n)
      max = n ;

    }
    cout <<endl<<"Largest num is ="<<max ;
  }


}

/*
5) Calculate Average of Numbers Using Arrays
*/
void Display_ArrayAverageElement ()
{
  int num =0;
  int max = 0;
  float sum =0;
  int arr[100] ={0} ;
  cout <<"Enter your num of elements between 1 and 100:" ;
  cin  >>num ;
  if (num <= 100 && num >=0){
    int n = 0;
    for ( int i =  0 ; i <num ; i ++){

      cout <<endl<<"Enter num:"<<i <<":";
          cin >>n ;
          arr[i] =n ;

    }

    for ( int i =  0 ; i <num ; i ++){

        sum+=arr[i] ;
    }
    cout <<endl<<"Average ="<<sum/num ;
  }


}


/*
6) Write a program and input two integers in main and pass them to
default constructor of the class. Show the result of the addition of two
numbers.
*/
class add {
  int n1 ;
  int n2 ;
  public :
  add(int num1 , int num2 ){
    n1 = num1 ;
    n2 = num2 ;
    cout <<"Numbers Initialized"<<endl ;
  }

  void add_num(){
    cout << "The addition result on :" <<n1 + n2 ;
  }

};

void call_add_Class (){
  int num_1 ;
  int num_2 ;
  cout <<"Enter first number :" ;
  cin >>num_1 ;
  cout <<"Enter second number :" ;
  cin >>num_2 ;
add a1(num_1 ,num_2) ;
  a1.add_num();
}

/*
7) Perform addition operation on complex data using class and object.
The program should ask for real and imaginary part of two complex
numbers, and display the real and imaginary parts of their sum.
*/

class Complex_Data{
int Real ;
int Img ;
public :
  Complex_Data (){
    cout<<"Enter the real part :" ;
    cin >>Real ;
    cout<<"Enter the Img part :"  ;
    cin >>Img ;
  }
  int get_real () {

    return (Real);
  }

  int get_Img(){

    return(Img) ;
  }


};

void call_Complex_Data(){
  cout <<"First number" <<endl ;
Complex_Data D1 ;
cout <<"second number" <<endl ;
Complex_Data D2 ;
cout <<"The sum of real part is "<<D1.get_real()+D2.get_real() <<endl ;
cout <<"The sum of Imag part is "<<D1.get_Img()+D2.get_Img() <<endl ;

}
