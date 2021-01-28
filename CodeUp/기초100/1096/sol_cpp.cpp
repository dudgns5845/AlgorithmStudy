#include <iostream>
using namespace std;
 
int main() 
{
    int board[20][20] ={0,};
    int input;
    scanf("%d",&input);

    for(int i = 0 ; i<input ;i++){
        int x, y;
        scanf("%d %d",&x,&y);
        board[x][y] = 1;
    }

    for(int i = 1 ; i < 20 ; i++){
        for(int j = 1 ; j<20;j++){
            printf("%d ",board[i][j]);
        }
        cout<<endl;
    }

    return 0;
}
