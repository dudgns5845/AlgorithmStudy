#include<bits/stdc++.h>

using namespace std;

int n, m;
string a, b;
int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		map<string, int> _map;
		cin >> m;
		for (int i = 0; i < m; i++) {
			cin >> a >> b;
			_map[b]++;
		}

		long long ret = 1;
		for (auto c : _map) {
			ret *= ((long long)c.second + 1);
		}
		//아무것도 입지 않는 경우수 빼주기
		ret -= 1;
		
		cout << ret << '\n';

	}

	return 0;
}