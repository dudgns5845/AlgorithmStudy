#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%d",&input);

	if(input <= 39) printf("D\n");
	else if(input <= 69) printf("C\n");
	else if(input <= 89) printf("B\n");
	else printf("A\n");
	
	return 0;
}
