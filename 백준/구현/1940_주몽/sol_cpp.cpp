#include<bits/stdc++.h>
using namespace std;
int N, M,temp,cnt;
vector<int> v;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		
		cin >> temp;
		v.push_back(temp);
	}

	sort(v.begin(), v.end());

	if (M > 200000) cout << 0 << '\n';
	else {
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				if (v[i] + v[j] == M) cnt++;
			}
		}
		cout << cnt << '\n';
	}


	return 0;
}