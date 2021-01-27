#include<iostream>
using namespace std;

int main()
{	
	char input,start;
	start = 'a';
	scanf("%c",&input);

	do{
		printf("%c ",start);
	}while(input != start++);
	return 0;
}
