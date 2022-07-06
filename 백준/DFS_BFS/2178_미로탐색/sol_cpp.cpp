#include<bits/stdc++.h>

using namespace std;

int N, M;
int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int board[101][101] = {0,};
int visited[101][101] = {0,};

int main(){
   
    cin>>N>>M;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M;j++){
            //연속되어도 하나씩 입력받는 방법
            scanf("%1d",&board[i][j]);
        }
    }

    queue<pair<int,int>> q;
    visited[0][0] = 1;

    //시작위치 넣기
    q.push({0,0});

    while(q.size()){
        int x,y;
        tie(x,y) = q.front();
        q.pop();

        for(int i = 0 ; i < 4 ; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || ny < 0 || nx >= N || ny >= M || board[nx][ny] == 0) continue;
            if(visited[nx][ny]) continue;
        
            visited[nx][ny] = visited[x][y]+1;
            q.push({nx,ny});
            
        }
    }

    cout << visited[N-1][M-1]<<'\n';
}