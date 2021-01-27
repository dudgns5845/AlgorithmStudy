#include <iostream>
using namespace std;
 
int main() 
{
    int input;
    int input_ary[10000]={0,};
    int temp;
    scanf("%d",&input);
    for(int i = 0 ; i < input ; i++ ){
        scanf("%d",&temp);
        input_ary[temp]+=1;
    }

    for(int i = 1 ; i <= 23 ; i++){
        printf("%d ",input_ary[i]);
    }
    return 0;
}
