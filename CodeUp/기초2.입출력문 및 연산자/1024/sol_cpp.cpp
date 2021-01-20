#include<iostream>
using namespace std;

int main()
{
	char input[21];
	scanf("%s",input);
	int i = 0 ; 
	while(input[i]!='\0'){
		printf("'%c'\n",input[i++]);
	}

	return 0;
}
