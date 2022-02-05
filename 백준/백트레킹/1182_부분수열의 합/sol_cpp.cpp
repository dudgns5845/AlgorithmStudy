#include <iostream>

using namespace std;

#define MAX_N 21

int n, sum;
int num[MAX_N];
int ans;

void sub(int i, int prev_Sum)
{
    // index를 끝까지 했으면 종료
    if (i == n)
    {
        // sum과 같으면 ans++
        if (prev_Sum == sum)
            ans++;
        return;
    }

    // 숫자를 사용하는 경우
    sub(i + 1, prev_Sum + num[i]);
    // 사용하지 않는 경우
    sub(i + 1, prev_Sum);

}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0); 
    cout.tie(0);

    cin >> n >> sum;

    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }

    sub(0, 0);

    if (sum == 0) ans -= 1;

    cout << ans << "\n";

    return 0;
}