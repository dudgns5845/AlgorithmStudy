#include <iostream>
#include <deque>

using namespace std;
int T;
int board_size;
int dx[8] = { -2,-2,-1,-1,+1,+1,+2,+2 };
int dy[8] = { -1,+1,-2,+2,-2,+2,-1,+1 };

int bfs();

int main() {
	cin >> T;

	for (int i = 0; i < T; i++) {
		cout << bfs() << endl;
	}
}

int bfs() {
	//방문 여부 및 거리 저장
	int visited[300][300] = { 0, };
	//방문할 목록 
	deque<pair<int, int>> que;
	//보드 크기 입력
	cin >> board_size;

	//시작 위치 목적지 입력
	pair<int, int> start_pos;
	pair<int, int> end_pos;
	cin >> start_pos.first >> start_pos.second;
	cin >> end_pos.first >> end_pos.second;

	//처음 시작 위치 입력
	que.push_back(start_pos);

	//탐색 시작
	while (!que.empty()) {
		pair<int, int> now_pos = que.front();
		que.pop_front();
		//printf("방문 좌표 : %d %d\n", now_pos.first, now_pos.second);
		//탐색 시작 위치가 목적지랑 같으면 종료
		if (now_pos == end_pos) return visited[now_pos.first][now_pos.second];
		//다음 탐색 경로를 추가하자
		else {
			for (int i = 0; i < 8; i++) {
				int new_dx = now_pos.first + dx[i];
				int new_dy = now_pos.second + dy[i];
				if (0 <= new_dx && new_dx < board_size && 0 <= new_dy && new_dy < board_size) {
					//다음 방문하는 곳이 간 곳이 아니라면
					if (visited[new_dx][new_dy] == 0) {
						//printf("입력 좌표 : %d %d\n", new_dx, new_dy);
						//추가해주자
						que.push_back({ new_dx,new_dy });
						//그리고 그곳을 방문 표시 및 거리 추가
						visited[new_dx][new_dy] = visited[now_pos.first][now_pos.second]+1;
					}
				}
			}
		}
	}
	return 0;
}
