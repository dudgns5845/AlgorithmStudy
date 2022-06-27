#include <bits/stdc++.h>
using namespace std;

int dp[1004][2][34], n, m, b[1004];

int sol(int idx, int tree, int cnt)
{
    if (cnt < 0)
        return -1e9;
    if (idx == n)
        return cnt == 0 ? 0 : -1e9;

    int &ret = dp[idx][tree][cnt];
    if (~ret)
        return ret;

    return ret = max(sol(idx + 1, tree ^ 1, cnt - 1), sol(idx + 1, tree, cnt) + (tree == b[idx] - 1));
}

int main()
{
    memset(dp, -1, sizeof(dp));
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> b[i];
    cout << max(sol(0, 1, m - 1), sol(0, 0, m)) << '\n';
    return 0;
}