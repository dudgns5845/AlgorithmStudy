#include <iostream>
using namespace std;

int input[100000];
int dp[100000];

int main(){

    int T;
    int MAX;
    cin >> T;
    for(int i = 0 ; i < T; i++){
        cin >>input[i];
    }
    MAX = input[0];

    for(int i = 0 ; i < T ; i++ ){
        dp[i] = input[i];
        if(i == 0) continue;
        if(dp[i] < dp[i-1] + input[i]){
            dp[i] = dp[i-1] + input[i];
        }
        if(dp[i] > MAX) MAX = dp[i];
    }
    cout << MAX << "\n";
}