#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int M, N;
string s;
map<string, int> _map;
map<int, string> _map2;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> s;
		_map[s] = i + 1;
		_map2[i + 1] = s;
	}

	for (int i = 0; i < M; i++) {
		cin >> s;
		//문자열이면
		if (atoi(s.c_str()) == 0) {
			cout << _map[s] << '\n';
		}
		else {
			cout << _map2[atoi(s.c_str())] << '\n';
		}
	}

	return 0;
}