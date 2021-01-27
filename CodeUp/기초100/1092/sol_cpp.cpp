#include <iostream>
using namespace std;
 
int main() 
{
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    int i = 1;
    while(true){
        if(i%a == 0 && i%b == 0 && i%c == 0 ){
            printf("%d",i);
            break;
        }
        i++;
    }
    return 0;
}
