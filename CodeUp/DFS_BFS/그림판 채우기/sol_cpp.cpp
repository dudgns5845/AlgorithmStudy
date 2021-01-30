#include <iostream>
using namespace std;

//전역에 선언 --> 접근의 용이를 위해
char board[11][11];

//색 채워가는 함수
void paint(int row, int col){
    //범위를 벗어남
    if (row == -1 || row == 10 || col == -1 || col == 10){
        return ;
    }

    //이미 색칠되어있으니 패스
    if(board[row][col] == '*'){
        return;
    }

    //안칠해져있으니 채워주기
    if(board[row][col] == '_'){
        board[row][col] = '*';
    }
    
    //상하좌우를 점검
    paint(row-1,col);
    paint(row+1,col);
    paint(row,col+1);
    paint(row,col-1);

    return ;
}

int main(){
   
    int x,y;

    //c++의 문자열 입력을 받는게 계속 헷갈린다...
    for(int i = 0 ; i < 10 ; i++){
        //라인 한줄 받기
        scanf("%s",board[i]);
    }

    scanf("%d %d",&x,&y);

    //왜냐면 시각적으로는 x는 오른쪽 y는 왼쪽으로 설정했기에 반대로 입력해줘야한다.
    paint(y,x);

    for(int i = 0 ; i< 10 ; i++){
        for(int j = 0 ; j < 10 ;j ++){
            printf("%c",board[i][j]);
        }
        cout<<endl;
    }
    return 0;

}