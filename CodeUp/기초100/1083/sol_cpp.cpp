#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%X",&input);

	for(int i = 1 ; i<=input ;i++){
		if(i % 3 == 0){	
			printf("X ");
		}else{
			printf("%d ",i);
		}
	}

	return 0 ;
}
