#include<bits/stdc++.h>
using namespace std;

string str, temp;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> str;
	temp = str;
	reverse(str.begin(), str.end());
	int ret = temp == str ? 1 : 0;
	cout << ret;
}