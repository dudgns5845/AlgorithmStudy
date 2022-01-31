#include <iostream>
using namespace std;

int input;
int dp_a[50] = {
    0,
};
int dp_b[50] = {
    0,
};

void DP();

int main()
{
    cin >> input;

    DP();
    return 0;
}

void DP()
{

    dp_a[0] = 1;
    dp_a[1] = 0;
    dp_b[0] = 0;
    dp_b[1] = 1;

    for (int i = 2; i <= input; i++)
    {
        dp_a[i] = dp_b[i-1];
        dp_b[i] = dp_b[i-1] + dp_a[i-1];
        //cout<< dp_a[i] << " " << dp_b[i]<<endl; 
    }

    cout<< dp_a[input] << " " << dp_b[input]; 
}