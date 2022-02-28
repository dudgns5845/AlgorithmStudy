#include <iostream>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int dp[10001];
        for (int j = 0; j < 10001; ++j)
        {
            dp[j] = 0;
        }
        dp[0] = 1;
        int N;
        int coin[21];
        cin >> N;
        for (int j = 0; j < N; ++j)
        {
            cin >> coin[j];
        }
        int m;
        cin >> m;
        for (int j = 0; j < N; ++j)
        {
            for (int k = coin[j]; k <= m; ++k)
            {
                dp[k] += dp[k - coin[j]];
            }
        }
        cout << dp[m] << '\n';
    }
    return 0;
}
