#include <iostream>

using namespace std;

int main() {

	int input_ary[10001] = {0,};
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		int temp;
		scanf("%d", &temp);
		input_ary[temp]++;
	}

	for (int i = 0; i < 10001; i++) {
		if (input_ary[i] != 0) {
			for (int j = 0; j < input_ary[i]; j++) {
				printf("%d\n", i);
			}
		}
	}

	return 0;
}