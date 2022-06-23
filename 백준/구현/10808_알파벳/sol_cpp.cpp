#include<bits/stdc++.h>

using namespace std;

string str;
int cnt[26]; //알파벳은 26개
int main() {
	ios_base::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);

	cin >> str;

	for (char a : str) {
		cnt[a - 'a']++;
	}

	for (int i : cnt) {
		cout << i << " ";
	}

	return 0;
}