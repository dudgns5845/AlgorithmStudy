#include <iostream>
using namespace std;
 
int main() 
{
    int board[11][11];
    for(int i = 1 ; i<=10;i++){
        for(int j = 1 ; j<=10;j++){
            scanf("%d",&board[i][j]);
        }
    }

    int x = 2;
    int y = 2;

    while(true){
        //미방문 구역
        if(x > 10 || y > 10) break;
        if(board[x][y]==0){
            board[x][y] = 9;
        } 
        //먹이 찾음
        else if(board[x][y]==2){
            board[x][y] = 9;
            break;
        }
        //막힌 구간
        else if(board[x][y] == 1){
            x++;
            y--;
            continue;
        }
        y++;
    }

    for(int i = 1 ; i<=10;i++){
        for(int j = 1 ; j<=10;j++){
            printf("%d ",board[i][j]);
        }
        cout<< endl;
    }
    return 0;
}
