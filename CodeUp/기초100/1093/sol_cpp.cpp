#include <iostream>
using namespace std;
 
int main() 
{
    int input;
    int ary[10000]={0,};
    scanf("%d",&input);
    int temp;
    for(int i = 0;i<input ;i++){
        scanf("%d",&temp);
        ary[i] = temp;
    }

    for(int i = input-1 ; i>= 0 ; i--){
        printf("%d ",ary[i]);
    }
    return 0;
}
