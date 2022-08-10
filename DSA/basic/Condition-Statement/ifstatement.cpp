#include <iostream>
using namespace std;


int main(){
    int Money =300;
    cout << "Enter The Amount" << endl;

     cin >> Money ;

     if(Money < 500){
        cout << "You need to go with bus to collage" << endl;
     }
     else if (Money > 500)
     {
        cout << "You can go to Collage with Bike " << endl;
        
        if(Money > 1200){
         cout << "You can Take Bullet" << endl;
        }
        else {
         cout << "we have only ride Splender in this amount" << endl;
        }
     }  
     return 0;
}
