#include <iostream>
using namespace std;
 
int main() 
{
    int h,w;
    int n;
    int l,d,x,y;
    int board[101][101]={0,};


    scanf("%d %d",&h,&w);
    scanf("%d",&n);

    for(int i = 1; i<=n;i++){
        scanf("%d %d %d %d",&l,&d,&x,&y);

        //d==0은 가로
        if(d ==0){
            for(int j = 0 ; j<l;j++){
                board[x][y+j] = 1;
            }
        }
        //d==1은 세로
        else{
            for(int j = 0 ; j<l;j++){
                board[x+j][y] = 1;
            }
        }
    }

    for(int i = 1 ; i<= h;i++){
        for(int j = 1 ; j <= w; j++){
            printf("%d ",board[i][j]);
        }
        cout<<endl;
    }
    return 0;
}
