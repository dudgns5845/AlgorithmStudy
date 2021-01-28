#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    int n,m;
    scanf("%d %d",&n,&m);

    int ary[101][101];

    int result = 0;

    for (int i = 0 ; i < n ; i++){
        for(int j = 0 ; j<m ; j++){
            scanf("%d",&ary[i][j]);
        }
    }

    for (int i = 0 ; i < n ; i++){
        int min = 10000000;
        for(int j = 0 ; j < m ; j++){
            if(ary[i][j]<min){
                min = ary[i][j];
            }
        }
        if(result < min){
            result = min;
        }
    }

    printf("%d",result);

    return 0;

}