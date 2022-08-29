#include<iostream>
using namespace  std ;

void recta(int num){
//Rectangle Pattern    
// ****
// ****
// ****
// ****
     for(int i=0;i<num;i++){
        for(int j=0;j<num;j++){
            printf("*");
        }
        printf("\n");
    }

}
//  ****
//  *  *
//  *  *
//  ****

void hollowRectangle(int num){

   for(int i=0;i<num;i++){
        for(int j=0;j<num;j++){
            if (i==0 or j==0 or i==num-1 or j==num-1){
                 printf("*");

            }
            else {
                printf(" ");
           
        }
        
    }
    printf("\n");
}
}

void triangle(int num){
// # *
// # **
// # ***
// # ****
// # *****
for(int i=0;i<num;i++){
    for(int j=0;j<i+1;j++){
        printf("*");
    }
    printf("\n");
}

}

void halfpramid(int num){
    
// # Half Pramid Number
// # 1
// # 2 2
// # 3 3 3
// # 4 4 4 4
for(int i=1;i<=num;i++){
    for(int j=1;j<i+1;j++){
        cout<<i ;
    }
    cout<<"\n";
}
}

int main()
{
    int n=4;
//    printf("Print Recrtangle:\n");
//    recta(n);
//  printf("Print hollowRectangle:\n");
//    hollowRectangle(n);
// printf("Print Triangle:\n");
// triangle(n);
printf("Print halfpramid:\n");
halfpramid(n);
   return 0;

}
    
  
