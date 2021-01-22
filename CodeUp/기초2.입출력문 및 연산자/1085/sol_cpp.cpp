#include<iostream>
using namespace std;

int main()
{
	long long h,b,c,s;
	scanf("%lld %lld %lld %lld",&h,&b,&c, &s);
	printf("%.1lf MB",h*b*c*s/((float)1024*1024*8));
	return 0;
}

