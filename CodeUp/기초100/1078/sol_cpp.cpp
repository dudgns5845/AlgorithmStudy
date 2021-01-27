#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%d",&input);
	int i = 1;
	int sum = 0;
	while(i<=input){
		if(i%2 ==0){
			sum+=i;
		}
		i++;
	}
	printf("%d",sum);
	return 0;
}
