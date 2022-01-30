#include <iostream>

using namespace std;

char board[8][8];

int main() {

	for (int i = 0; i < 8; i++) {
		cin >> board[i];
	}

	int answer = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = i%2; j < 8; j += 2) {
			if (board[i][j] == 'F') {
				answer++;
			}
		}
	}

	cout << answer;
	return 0;
}