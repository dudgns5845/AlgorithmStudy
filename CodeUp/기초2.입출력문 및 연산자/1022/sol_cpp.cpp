#include<iostream>
using namespace std;

int main()
{
	char input[2001];
	//fgets()
	//문자를 입력할때 라인 전체 즉 빈칸도 허용해서 저장할때 사용한다.
	fgets(input,2000,stdin);
	printf("%s",input);
	return 0;
}
