#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%X",&input);
	int i = 1;

	while(i<16){
		printf("%X*%X=%X\n",input,i++,input*i);
	}

	return 0 ;
}
