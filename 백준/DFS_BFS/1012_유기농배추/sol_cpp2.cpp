#include <bits/stdc++.h>
using namespace std;

int T,M,N,K,ret;
int board[51][51] = {0,};
int visited[51][51] = {0,};

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

void dfs(int x, int y){
    visited[x][y] = 1;
    for(int i = 0 ; i<4 ; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx < 0 || nx >= M || ny< 0 || ny>=N) continue;
        if(visited[nx][ny]== 0 && board[nx][ny] != 0){
            dfs(nx,ny);
        }
    }
}

int main(){
    cin >> T;
    
    while(T--){

        //초기화
        for(int i = 0 ; i<51;i++){
            for(int j = 0 ; j <51 ;j++){
                board[i][j] = 0;
                visited[i][j] = 0;
            }
        }
        ret = 0;

        cin >> M >> N >> K;

        for(int i = 0 ; i<K ; i++){
            int x,y;
            cin >>x>>y;
            board[x][y] = 1;
        }

        for(int i = 0 ; i< M ; i++){
            for(int j = 0 ; j< N ; j++){
                if(visited[i][j] == 0 && board[i][j] != 0){
                    dfs(i,j);
                    ret++;
                }
            }
        }
        cout<<ret<<'\n';
    }
}