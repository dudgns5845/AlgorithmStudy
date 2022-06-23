#include<bits/stdc++.h>
using namespace std;

int N, M;
int ary[4001];

void solution() {
	int a, b, c;
	cin >> a>> b>> c;
	switch (a) {
	case 1:
		ary[b] = c;
		break;
	case 2:
		for (; b <= c; b++) {
			ary[b] = ary[b] == 0 ? 1 : 0;
		}
		break;
	case 3:
		for (; b <= c; b++) {
			ary[b] = 0;
		}
		break;
	case 4:
		for (; b <= c; b++) {
			ary[b] = 1;
		}
		break;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> N >> M;
	//전구 상태
	for (int i = 1; i <= N; i++) {
		cin >> ary[i];
	}

	for (int i = 0; i < M; i++) {
		solution();
	}

	for (int i = 1; i <= N; i++) {
		cout << ary[i] << " ";
	}
}

