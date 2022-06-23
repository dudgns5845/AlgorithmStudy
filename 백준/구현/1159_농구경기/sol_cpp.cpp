#include<bits/stdc++.h>
using namespace std;

string input, ret;
int main() {

	getline(cin, input);

	for (int i = 0; i < input.size(); i++) {
		//대문자
		if (input[i] >= 65 && input[i] < 97) {
			if (input[i] + 13 > 90) input[i] -= 13;
			else input[i] += 13;
		}
		//소문자
		else if (input[i] >= 97 && input[i] <= 122) {
			if (input[i] + 13 > 122) input[i] -= 13;
			else input[i] += 13;
		}
		cout << input[i];
	}
	return 0;
}