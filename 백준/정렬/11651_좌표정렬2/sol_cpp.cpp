#include<iostream>
#include<utility>
#include<vector>
#include<algorithm>

using namespace std;

bool compare(pair<int, int>a, pair<int, int>b) {

	if (a.second == b.second) {
		return a.first < b.first;
	}
	return a.second < b.second;
}

int main() {
	int N;
	cin >> N;

	vector<pair<int, int>> input_list;

	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		input_list.push_back(make_pair(x, y));
	}
	//정렬 커스텀하기
	sort(input_list.begin(), input_list.end(), compare);

	vector<pair<int, int>> ::iterator iter;

	for (iter = input_list.begin(); iter != input_list.end(); iter++) {
		cout << iter->first << " " << iter->second << '\n';
	}

	return 0;
}