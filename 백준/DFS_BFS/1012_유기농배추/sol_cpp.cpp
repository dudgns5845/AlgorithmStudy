#include <iostream>
#include <deque>
using namespace std;

int board[50][50];
int visited[50][50];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
int T, M, N, K;
int answer = 0;
void BFS(int x, int j);

int main() {

	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> M >> N >> K;
		for (int j = 0; j < K; j++) {
			int x, y;
			cin >> x >> y;
			board[x][y] = 1;
		}

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == 1 && visited[i][j] == 0) {
					answer++;
					BFS(i, j);
				}
			}
		}

		cout << answer << "\n";
		answer = 0;

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				visited[i][j] = 0;
				board[i][j] = 0;
			}
		}
	}
}

void BFS(int new_x, int new_y) {

	deque<pair<int, int>> que;

	que.push_back({ new_x, new_y });

	while (!que.empty()) {

		int x = que.front().first;
		int y = que.front().second;
		visited[x][y] = 1;

		que.pop_front();

		for (int i = 0; i < 4; i++) {
			int temp_x = x + dx[i];
			int temp_y = y + dy[i];
			if (0 <= temp_x && temp_x < M  && 0 <= temp_y && temp_y < N  && visited[temp_x][temp_y] == 0 && board[temp_x][temp_y] == 1) {
				visited[temp_x][temp_y] = 1;
				que.push_back({ temp_x,temp_y });
			}
		}
	}
}