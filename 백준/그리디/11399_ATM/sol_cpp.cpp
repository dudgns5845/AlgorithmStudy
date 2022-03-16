#include <iostream>
#include<vector>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	vector<int> input;
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		input.push_back(temp);
	}

	sort(input.begin(), input.end());

	int sum = 0;
	int waitTime = 0;
	for (int i = 0; i < input.size(); i++) {
		waitTime += input[i];
		sum += waitTime;
	}

	cout << sum;

	return 0;
}