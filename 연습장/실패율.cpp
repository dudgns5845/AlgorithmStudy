#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

bool comp(const pair<double, int>& a, const pair<double, int>& b) {
	//실패율 먼저 비교(내림차순)
	if (a.first > b.first) {
		return true;
	}
	else if (a.first == b.first) {
		//실패율이 같다면 스테이지 번호를 비교(오름차순)
		if (a.second < b.second) {
			return true;
		}
		else {
			return false;
		}
	}
	else {
		return false;
	}
}

vector<int> solution(int N, vector<int> stages) {

	vector <int > answer;

	vector <int> record_stage(N+1);

	vector< pair<double, int> > record_fail;

	//사용자의 수 - 나중에 실패율 계산할때 사용
	int user = stages.size();

	//스테이지별 사용자 수 세기
	for (int i = 0; i < user; i++) {
		record_stage[stages[i]]++;
	}

	//이제 실패율을 계산할 차례
	for (int i = 1; i <= N; i++) {
		
		//스태이지의 유저가 0명일 경우
		if (record_stage[i] == 0 ||user ==0) {
			record_fail.push_back(make_pair(0, i));
			continue;
		}
		else {
			double rate = (double)record_stage[i] / user;
			record_fail.push_back(make_pair(rate, i));
			user -= record_stage[i];
		}
	}
	//(실패율 , 인덱스)
	//해야하는 일은 실패율을 최대로부터 정렬
	//실패율이 같은경우는 인덱스 오름차순
	sort(record_fail.begin(), record_fail.end(),comp);

	for (int i = 0; i < N; i++) {
		answer.push_back(record_fail[i].second);
	}


	return answer;
}