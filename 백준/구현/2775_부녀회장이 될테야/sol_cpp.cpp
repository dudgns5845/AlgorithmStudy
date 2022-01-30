#include<iostream>
using namespace std;

int board[16][16] = { 0, }; //전체 기록
int dp[16][16] = { 0, }; //방문 기록

void calculation();

int main() {

	calculation();

	int T, k, n;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> k >> n;
		cout << board[k][n] << "\n";
	}

	return 0;
}

void calculation() {

	for (int i = 0; i < 16; i++) {
		board[0][i] = i;
	}

	for (int i = 0; i < 15; i++) {
		for (int j = 1; j < 16; j++) {
			board[i + 1][j] = board[i][j] + board[i + 1][j - 1];
		}
	}
}

