#include <iostream>
using namespace std;
 
int main() 
{
    int size;
    int min=100000;
    scanf("%d",&size);

    for(int i = 0 ; i<size ; i++){
        int temp;
        scanf("%d",&temp);
        if(min > temp){
            min = temp;
        }
    }
    printf("%d",min);
    return 0;
}
