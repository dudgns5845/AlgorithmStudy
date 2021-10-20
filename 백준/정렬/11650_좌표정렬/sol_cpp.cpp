#include<iostream>
#include<utility>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<pair<int, int>> input_list;

	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		input_list.push_back(pair<int,int>(x,y));
	}

	sort(input_list.begin(), input_list.end());

	vector<pair<int, int>> ::iterator iter ;

	for (iter = input_list.begin(); iter != input_list.end(); iter++) {
		cout << iter->first << " " << iter->second << '\n';
	}
    // 시간 초과가 나서 찾아보다 endl과 \n의 차이를 알게됨
	/// <summary>
	/// 32번째 줄의 endl 은 flush 연산을 수행합니다.
	// flush 연산은 출력 버퍼에 남아있는 내용을 즉시 출력하는 연산으로, 매우 무거운 연산입니다.
	//	(인터렉티브 문제가 아니라면) 매 출력마다 flush 할 필요가 없습니다.
	//	endl 대신 "\n" 을 사용하세요.
	/// </summary>
	/// <returns></returns>
	return 0;
}