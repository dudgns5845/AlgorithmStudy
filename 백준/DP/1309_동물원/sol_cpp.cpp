#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

#define MAX 100001

int N;
int DP[MAX][3];

void init() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
}

int main() {
	init();
	cin >> N;
	DP[0][0] = DP[0][1] = DP[0][2] = 1;

	for (int i = 1; i < N; i++) {
		DP[i][0] = (DP[i - 1][0] + DP[i - 1][1] + DP[i - 1][2]) % 9901;
		DP[i][1] = (DP[i - 1][0] + DP[i - 1][2]) % 9901;
		DP[i][2] = (DP[i - 1][0] + DP[i - 1][1]) % 9901;
	}
	int result = (DP[N - 1][0] + DP[N - 1][1] + DP[N - 1][2]) % 9901;
	cout << result;

	return 0;
}