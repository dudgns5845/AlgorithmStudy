#include <iostream>

using namespace std;

int dp[46] = { 0, };

int Fibbo(int n) {
	if (n == 0) { return 0; }
	if (n == 1) { return 1; }
	if (dp[n] != 0) { return dp[n]; }
	else {
		dp[n] = Fibbo(n - 2) + Fibbo(n - 1);
		return dp[n];
	}
}

int main() {

	dp[1] = 1;
	dp[2] = 1;

	int n;
	cin >> n;
	
	cout << Fibbo(n);

	return 0;
}

