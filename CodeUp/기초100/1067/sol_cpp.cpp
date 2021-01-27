#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%d",&input);

	if(input < 0){
		printf("minus\n");
	}else{
		printf("plus\n");
	}
	if(input % 2 ==0){
		printf("even\n");
	}else{
		printf("odd\n");
	}
	return 0;
}
