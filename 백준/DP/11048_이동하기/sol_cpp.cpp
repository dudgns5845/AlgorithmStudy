#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int board[1001][1001] = { 0, };
int visited[1001][1001] = { 0, };


void DFS() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			int Max = max(max(visited[i - 1][j], visited[i][j - 1]), visited[i - 1][j - 1]);
			visited[i][j] = Max + board[i][j];
		}
	}
	cout << visited[N][M];
}


int main() {
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> board[i][j];
		}
	}

	DFS();
}