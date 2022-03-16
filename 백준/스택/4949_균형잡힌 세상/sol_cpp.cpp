#include <iostream>
#include <string>
#include <stack>

using namespace std;

void init() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
}

int main() {
	init();

	while (true) {
		string Text;
		getline(cin, Text);
		stack<char> s;
		bool answer = true;

		if (Text.size() == 1 && Text[0] == '.') break;
		for (int i = 0; i < Text.size(); i++) {
			if (Text[i] == '(' || Text[i] == '[') {
				s.push(Text[i]);
			}
			if (Text[i] == ')') {
				if (s.empty() || s.top() == '[') answer = false;
				else s.pop();
			}
			if (Text[i] == ']') {
				if (s.empty() || s.top() == '(') answer = false;
				else s.pop();
			}
		}
		if (s.empty() && answer == true) {
			cout << "yes" << "\n";
		}
		else {
			cout << "no" << "\n";
		}
	}
	return 0;
}