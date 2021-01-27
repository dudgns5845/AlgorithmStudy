#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%d",&input);
	int sum = 0;
	for(int i = 1 ; i<=input; i++){
		sum+=i;
		if(sum>= input){
			printf("%d",sum);
			break;
		}
	}
	return 0;
}
