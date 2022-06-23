#include<bits/stdc++.h>

using namespace std;

int A, B, C;
int cnt[104];
int ret;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> A >> B >> C;

	for (int i = 0; i < 3; i++) {
		int first, last;
		cin >> first >> last;
		for (int j = first; j < last; j++) {
			cnt[j]++;
		}
	}

	for (int i : cnt) {
		if (i == 1) {
			ret +=  A;
		}
		else if (i == 2) {
			ret += 2 * B;
		}
		else if (i == 3) {
			ret += 3 * C;
		}
	}
	cout << ret;
}
