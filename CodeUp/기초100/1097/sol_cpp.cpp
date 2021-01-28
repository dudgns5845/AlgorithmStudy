#include <iostream>
using namespace std;
 
int main() 
{
    int size;
    int x,y;
    int board[20][20];
    for(int i = 1; i<=19 ; i++){
        for(int j = 1; j<=19;j++){
            scanf("%d",&board[i][j]);
        }
    }

    scanf("%d",&size); //좌표 개수

    for(int i = 1; i<=size; i++){
        scanf("%d %d",&x,&y); //좌표 입력받기

        //가로줄 바꾸기
        for(int j = 1; j <= 19;j++){
            if(board[x][j] ==0){
                board[x][j] = 1;
            }else{
                board[x][j] = 0;
            }
        }
        //세로줄 바꾸기
        for(int j = 1; j <= 19;j++){
            if(board[j][y] == 0){
                board[j][y]=1;
            }else{
                board[j][y] = 0;
            }
        }
    }

    for(int i = 1; i<= 19 ;i ++){
        for(int j = 1;j<=19;j++){
            printf("%d ",board[i][j]);
        }
        cout<<endl;
    }
    return 0;
}
