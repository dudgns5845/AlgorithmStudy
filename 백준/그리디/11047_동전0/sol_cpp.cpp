#include <iostream>
using namespace std;

int coins[1000000];

int main()
{
    int N, K;
    int total_count = 0;
    cin >> N >> K;

    for (int i = 0; i < N; i++)
    {
        cin >> coins[i];
    }

    for (int i = N - 1; 0 <= i; i--)
    {
        if (coins[i] > K)
            continue;

        int temp = K / coins[i];
        K -= temp * coins[i];
        total_count += temp;
    }
    cout << total_count;
}