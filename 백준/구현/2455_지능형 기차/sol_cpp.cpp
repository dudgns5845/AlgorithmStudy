#include <iostream>
using namespace std;

int main() {
	int sum = 0;
	int max = 0;
	for (int i = 0; i < 4; i++) {
		int a, b;
		cin >> a >> b;
		sum = sum - a + b;

		if (sum > max) max = sum;
	}
	cout << max;
}