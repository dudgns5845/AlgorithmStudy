#include <iostream>
#include <algorithm>

int n;
int input[10001] = {0,};
int dp[10001] = {0,};
using namespace std;

int DP();

int main(){

    cin >> n;
    for(int i = 1 ; i <=n ; i++){
        cin >> input[i];
    }

    cout << DP();

    return 0;
}

int DP(){
    
    dp[1] = input[1];
    dp[2] = input[2] + dp[1];

    for(int i = 3 ; i <= n ; i++){
        dp[i] = dp[i- 1];
        dp[i] = max(dp[i],dp[i-2]+input[i]);
        dp[i] = max(dp[i],dp[i-3] + input[i-1]+input[i]);
    }
    return dp[n];
}