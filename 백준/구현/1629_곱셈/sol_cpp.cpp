//분할정복
#include <iostream>

using namespace std;

long long A, B, C;
int result = 0;

long long DC(int A, int B, int C) {
	if (B == 0) return 1;
	//재귀를 반복하며 최소한으로 쪼개진다
	long long temp = DC(A, B / 2, C);
	//나머지 연산을 한번하고
	temp = temp * temp % C;
	//B가 짝수 일때 
	if (B % 2 == 0) return temp;
	//B가 홀수 일때
	else if (B % 2 != 0) return temp * A % C;
}

int main() {
	
	cin >> A >> B >> C;
	cout << DC(A, B, C);

	return 0;
}