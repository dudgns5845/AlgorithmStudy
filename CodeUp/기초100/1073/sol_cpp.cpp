#include<iostream>
using namespace std;

int main()
{	
	int input;
reinput:
	scanf("%d",&input);

	if(input == 0) return 0;
	else {
		printf("%d\n",input);
		goto reinput;
	}
}
