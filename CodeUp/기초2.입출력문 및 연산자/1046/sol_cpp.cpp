#include<iostream>
using namespace std;

int main()
{
	long long a,b,c;
	scanf("%lld %lld %lld",&a,&b,&c);
	printf("%d\n%.1lf",(a+b+c), (float)(a+b+c)/3);
	return 0;
}

