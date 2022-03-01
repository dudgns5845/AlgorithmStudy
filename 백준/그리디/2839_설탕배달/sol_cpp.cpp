#include <iostream>

using namespace std;

int main()
{

    int N;
    int answer = 0;
    cin >> N;

    while (true)
    {
        if (N % 5 == 0)
        {
            answer += N/5;
            N /= 5;
            cout << answer << "\n";
            break;
        }

        N -= 3;
        answer++;
        
        if (N == 0)
        {
            cout << answer << "\n";
            break;
        }
        if (N < 0)
        {
            cout << -1;
            break;
        }
    }
}
