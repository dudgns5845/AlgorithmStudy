#include <iostream>

using namespace std;

int main()
{

    int N;
    cin >> N;

    int i = 1;
    while (true)
    {
        if (i * (i - 1) / 2 + 1 <= N && N < i * (i + 1) / 2 + 1)
        {
            break;
        }
        i += 1;
    }

    int index = N - (i * (i - 1) / 2 + 1);
    int up, down;
    //홀수면 위에가 큼
    if (i % 2 == 1)
    {
        up = i - index;
        down = 1 + index;
        cout << up << "/" << down;
    }
    //짝수면 아래가 큼
    else
    {
        up = 1 + index;
        down = i - index;
    }

    cout << up << "/" << down;
    return 0;
}