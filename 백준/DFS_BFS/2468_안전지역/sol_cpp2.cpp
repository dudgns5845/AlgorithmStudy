#include<bits/stdc++.h>
using namespace std;

int N,ret;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int visited[101][101] = {0,};
int board[101][101] = {0,};

void dfs(int x,int y){
    visited[x][y] = 1;
    for(int i = 0 ; i < 4 ;i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(nx<0||ny<0||nx>=N||ny>=N) continue;
        if(board[nx][ny] != 0 && visited[nx][ny] == 0){
            dfs(nx,ny);
        }        
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; i++){
           cin >> board[i][j];
        }
    }

     for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; i++){
           if(board[i][j]< N){
                board[i][j] =0;
                visited[i][j] = 1;
           }
        }
    }

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; i++){
           if(board[i][j] !=0 && visited[i][j] == 0){
                dfs(i,j);
                ret++;
           }
        }
    }
    cout << ret << '\n';
    return 0;
}