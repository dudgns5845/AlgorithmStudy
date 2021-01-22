#include<iostream>
using namespace std;

int main()
{
	long long r,g,b;
	scanf("%lld %lld %lld %lld",&r,&g,&b);
	printf("%.2lf MB",r*g*b/((float)1024*1024*8));
	return 0;
}

