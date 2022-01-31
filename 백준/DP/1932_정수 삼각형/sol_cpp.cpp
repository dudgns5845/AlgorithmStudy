#include <iostream>
#include <algorithm>
using namespace std;

int input[500][500] = {
    0,
};
int dp[500][500] = {
    0,
};
int n;

int DP();

int main()
{

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cin >> input[i][j];
        }
    }

    cout << DP() << "\n";

}

int DP()
{
    for (int i = n - 1; i >= 0; i--)
    {
        for (int j = 0; j <= i; j++)
        {
            if (i == n - 1)
            {
                dp[i][j] = input[i][j];
            }
            else
            {
                dp[i][j] = input[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
    }
    return dp[0][0];
}