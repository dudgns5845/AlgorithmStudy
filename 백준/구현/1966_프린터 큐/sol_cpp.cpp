#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int T;

int solution();

int main() {

	cin >> T;

	for (int i = 0; i < T; i++) {
		cout << solution() << "\n";
	}

	return 0;
}

int solution() {
	int answer = 1;

	//N은 인쇄 목록 개수
	//M은 확인하고 싶은 작업 위치
	int N, M;
	cin >> N >> M;

	deque<pair<int, int>> que(N);
	deque<int> record;
	int max = 0;
	//중요도 입력받기
	for (int i = 0; i < N; i++) {
		que[i].second = i;
		cin >> que[i].first;
		record.push_back(que[i].first);
	}

	//가중치로 정렬
	sort(record.begin(), record.end());

	while (!que.empty()) {
		//record의 맨 마지막은 최댓값
		max = record[record.size() - 1];
		pair<int, int> temp = que[0];
		que.pop_front(); //일단 제거
	
		if (max == temp.first) {
			if (temp.second == M) {
				break;
			}
			else {
				record.pop_back();
				max = record[record.size() - 1];
				answer++;
			}
		}
		else if (max != temp.first) {
			que.push_back(temp); //안맞으면 다시 집어넣기
		}

	}

	return answer;
}