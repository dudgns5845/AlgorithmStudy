#include<bits/stdc++.h>
using namespace std;

int h, m, cooktime;

int main() {

	cin >> h >> m >> cooktime;

	if ((m + cooktime) / 60 != 0) {
		h += (m + cooktime) / 60;
		m = (m + cooktime) % 60;
		if (h >= 24) h -= 24;
	}
	else {
		m += cooktime;
	}
	
	cout << h << " " << m;
	return 0;
}