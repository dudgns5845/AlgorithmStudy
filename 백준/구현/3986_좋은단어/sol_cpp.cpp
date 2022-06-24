#include<bits/stdc++.h>
using namespace std;

int N,cnt;
string s;
int main() {

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> s;
		stack<char> stk;
		for (char a : s) {
			if (stk.size() != 0 && stk.top() == a) stk.pop();
			else stk.push(a);
		}
		if (stk.size() == 0) cnt++;
	}

	cout << cnt << '\n';

	return 0;
}