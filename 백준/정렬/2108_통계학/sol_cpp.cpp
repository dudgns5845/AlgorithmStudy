#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {

	int N;
	cin >> N;

	vector <int> v; //값 저장
	int num[10001] = {0,}; //체크리스트

	double size = N;
	double sum = 0; //합
	int max = -4001;
	int min = 4001	; //최대최소

	for (int i = 0; i < N; i++) {
		int temp;
		scanf("%d", &temp);
		sum += temp; //값 더하고
		if (temp > max) max = temp;
		if (temp < min) min = temp;

		num[temp + 4000] += 1; //음수 인덱스를 위한 솔루션 0 = -4000, 1 = -3999 , 2 = -3998,,,

		v.push_back(temp);
	}

	//최대 빈도수
	int result = *max_element(num, num + 10000);
	int rep;
	int cnt = 0;

	for (int i = 0; i < 8001; i++) {
		if (cnt == 2)break;
		if (num[i] == result) {
			rep = i;
			cnt++;
		}
	}

	rep -= 4000;

	sort(v.begin(), v.end());

	cout << round((double)(sum / size)) << "\n";
	cout << v[size / 2] << "\n";
	cout << rep << "\n";
	cout << max - min << "\n";

	return 0;
}