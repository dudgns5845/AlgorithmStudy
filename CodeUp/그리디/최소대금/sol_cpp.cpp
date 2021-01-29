#include <iostream>
using namespace std;

int main(){
    int pasta[3];
    int juice[2];
    float min = 1000000;
    for(int i = 0 ; i < 3;i++){
        scanf("%d",&pasta[i]);
    }
    for(int i = 0 ; i < 2 ; i++){
        scanf("%d",&juice[i]);
    }

    for(int i = 0 ; i < 3 ; i++){
        for(int j = 0 ; j < 3; j++){
            float temp = (pasta[i] + juice[j]) * 1.1;
            if(min>temp){
                min = temp;
            } 
        }
    }
    printf("%.1f",min);

    return 0;
}