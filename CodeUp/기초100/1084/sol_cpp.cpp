#include<iostream>
using namespace std;

int main()
{	
	int r,g,b;
	int count = 0;
	scanf("%d %d %d",&r,&g,&b);

	for(int i = 0 ; i < r ; i++ ){
		for(int j = 0; j < g ; j++){
			for(int z=0; z < b ; z++){
				printf("%d %d %d\n",i,j,z);
				count++;
			}
		}
	}
	printf("%d",count);
	return 0 ;
}
