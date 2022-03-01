#include<iostream>
#include<queue>
#define MAX 101
using namespace std;
int map[MAX][MAX];
int visit[MAX][MAX];
int N,lim=1,cnt;
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};
queue<pair<int,int>> q;
void bfs(){
    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();
        for(int i=0;i<4;i++){
            int nextX=x+dx[i];
            int nextY=y+dy[i];
            if(nextX<0||nextX>=N||nextY<0||nextY>=N)continue;
            if(!visit[nextY][nextX]){
                visit[nextY][nextX]=1;
                q.push({nextX,nextY});
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    int res=1;
    cin>>N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin>>map[i][j];
            lim=lim<map[i][j]?map[i][j]:lim; 
        }
    }
    for(int i=0;i<lim;i++){
        for(int j=0;j<N;j++){
            for(int k=0;k<N;k++){
                visit[j][k]=i>=map[j][k]?1:0;
            }
        }
        cnt=0;
        for(int j=0;j<N;j++){
            for(int k=0;k<N;k++){
                if(!visit[j][k]){
                    q.push({k,j});
                    bfs();
                    cnt++;
                }
            }
        }
        if(res<cnt)res=cnt;
    }
    cout<<res;
}
