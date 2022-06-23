#include<bits/stdc++.h>

using namespace std;

int ary[31] = { 0, };

int main() {
	for (int i = 0; i < 28; i++) {
		int idx;
		cin >> idx;
		ary[idx] = 1;
	}

	for (int i = 1; i <= 30; i++) {
		if (ary[i] == 0) cout << i << "\n";
	}
}