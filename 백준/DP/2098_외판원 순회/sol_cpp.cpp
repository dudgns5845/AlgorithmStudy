#include <iostream>
using namespace std;
 
const int INF = 987654321;
int N;
int W[17][17];
int dp[16][1<<16];
 
int TSP(int curr, int visited){ //현재 도시가 curr이고, curr을 포함해서 방문했었던 도시들을 표현한게 visited일때, 
//앞으로 가야할 길 중에 최소를 구하는거다.
    int result;
    int ret = dp[curr][visited];
    if(ret!=0)
        return ret; //앞으로 다 돌기까지 남은 길 중에 최솟값을 미리 구해놨다면, 그 경로가 최소임이 자명하므로, 
 //메모이제이션을 통해 저장된 값 불러옴.
    //다 돌고 처음 도시로 돌아가는 경우
    if(visited==((1<<N)-1)){
        if(W[curr][0]!=0)
            return W[curr][0];
        return INF;
    }
 
    ret=INF;
    for(int i=0; i<N;i++){
        if(W[curr][i]==0 || (visited&(1<<i))) //1. 길이 없거나, 2. 한번방문한 도시(i)를 다시 방문하려고 한다면 --> 건너뛰어야함
            continue;
        ret = min(ret,W[curr][i]+TSP(i,visited|1<<i)); // curr-->i로 간다음에 i에서 나머지 도시들 순회한거 중 최소 or 
 //지금 값. 2개중 최소를 가림
    }
    dp[curr][visited]=ret; //최소화된 값을 dp배열에 메모이제이션
    return ret;
}
 
int main(void){
    cin>>N;
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            cin>>W[i][j];
 
    cout<<TSP(0,1);
}
