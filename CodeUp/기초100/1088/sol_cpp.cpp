#include<iostream>
using namespace std;

int main()
{	
	int input;
	scanf("%d",&input);
	for(int i = 1 ; i<= input ; i++){
		if(i%3==0){
			continue;
		}
		printf("%d ",i);
	}
	return 0;
}
