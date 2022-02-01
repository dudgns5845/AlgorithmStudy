#include <iostream>
#include <deque>

using namespace std;

int N, K;
deque<int> dq; //연산 과정을 기록할 덱
int visited[100001] = { 0, }; //방문 표시
int MAX = 100001; //최댓값

void bfs();
int main() {
	
	cin >> N >> K;
	
	bfs();
	
	return 0;
}

void bfs() {

	//1.나의 시작 위치 입력
	dq.push_back(N);

	//2.dq의 목록이 비거나, 목적지에 도달할때까지 반복
	while (!dq.empty()) {
		//맨 앞값 받고
		int start = dq.front();
		//탐색 목록에서 삭제
		dq.pop_front();

		//다음 방문하는 곳이 방문지라면 결과 출력하고 종료
		if (start == K) {
			cout << visited[start] << endl; 
			return;
		}

		//다음 방문할 곳이 이동 범위 안이며 방문하지 않았다면
		//count+1해서 저장
		if ( 0 <= start - 1 && start-1 < MAX && visited[start-1] == 0 && start - 1 != N) {
			visited[start - 1] = visited[start] + 1;
			dq.push_back(start - 1);
		}
		if (0 <= start + 1 && start + 1 < MAX && visited[start + 1] == 0 && start + 1 != N) {
			visited[start + 1] = visited[start] + 1;
			dq.push_back(start + 1);
		}
		if (0 <= start *2 && start *2 < MAX && visited[start*2] == 0 && start*2 != N) {
			visited[start*2] = visited[start] + 1;
			dq.push_back(start*2);
		}
	}
}
