#include<bits/stdc++.h>
using namespace std;
int N;
string ori_s,s, pre, suf;
int main() {

	cin >> N >> ori_s;
	//인덱스 찾고
	int pos = ori_s.find('*');
	pre = ori_s.substr(0, pos);
	suf = ori_s.substr(pos + 1); //2번째 파라미터 안적으면 끝까지

	for (int i = 0; i < N; i++) {
		cin >> s;
		if (pre.size() + suf.size() > s.size()) {
			cout << "NE\n";
		}
		else {
			if (pre == s.substr(0, pre.size()) && suf == s.substr(s.size() - suf.size())) {
				cout << "DA\n";
			}
			else {
				cout << "NE\n";
			}
		}
	}
	return 0;
}