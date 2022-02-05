//백트레킹도 dfs로 풀면 된다
#include <iostream>
using namespace std;
#define MAX 9

int N, M;
int board[MAX];
bool visited[MAX];

void DFS(int);

int main() {
	cin >> N >> M;
	DFS(0);
}

void DFS(int k) {
	
	//해당 뎁스까지 가면 출력
	if (M == k) {
		for (int i = 0; i < M; i++) {
			cout << board[i] << " ";
		}
		cout << "\n";
	}
	//여기가 사실상 처음 시작부분
	//아니면 한 레벨 더 진입
	else {
		//최상단 노드를 결정
		for (int i = 1; i <= N; i++) {
			//방문 안했으면 진입
			if (visited[i] == false) {
				visited[i] = true;
				board[k] = i; //저장하고 
				DFS(k + 1); //아래 뎁스로 진입 //여기서 계속 진입하다 길이를 다채우면 밑에 함수가 진행
				//여기가 중요
				//다시 초기화하는 과정
				visited[i] = false;
			}
		}
	}
}

