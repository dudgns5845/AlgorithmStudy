#include <iostream>
using namespace std;

int main(){
    int n, k;
    scanf("%d %d",&n,&k);
    int count = 0;

    while(n != 1){
        if(n % k != 0){
            count += n % k; //결국에는 나머지만큼 -1을 해줄 것이므로
            n -= n%k;
        }
        else{
            count +=1;
            n /= k;
        }
    }
    printf("%d",count);
    return 0;
}