#include<bits/stdc++.h>

using namespace std;

int T, N, max, min;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		vector<int> input;
		for (int j = 0; j < N; j++) {
			int temp;
			cin >> temp;
			input.push_back(temp);
		}
		sort(input.begin(), input.end());
		cout <<*(input.begin()) << " " << *(input.end()-1) << "\n";
	}
	return 0;
}