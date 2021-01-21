#include<iostream>
using namespace std;

int main()
{
	long long a, b;
	scanf("%lld %lld",&a,&b);
	printf("%lld\n",a+b);
	printf("%lld\n",a-b);
	printf("%lld\n",a*b);
	printf("%lld\n",a/b);
	printf("%lld\n",a%b);
	printf("%.2lf\n",(float)a/b);
	return 0;
}

