#include<iostream>
using namespace std;

int main()
{
	int a,b,c,d,e;
	//입력형식을 이용하여 입력값을 원하는데로 입력받기
	//c에서도 이런게 가능하구나... 몰랐네...
	scanf("%1d%1d%1d%1d%1d",&a,&b,&c,&d,&e);
	printf("[%d]\n",a*10000);
	printf("[%d]\n",b*1000);
	printf("[%d]\n",c*100);
	printf("[%d]\n",d*10);
	printf("[%d]\n",e);
	return 0;
}
