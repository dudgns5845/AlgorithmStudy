#include<iostream>
#include<string>

using namespace std;

int main()
{	
	string A_s = "best!!!";
	string B_s = "good!!";
	string C_s = "run!";
	string D_s = "slowly~";

	char input;
	scanf("%c",&input);

	switch (input)
	{
	case 'A':
	cout<<A_s;
		break;
	case 'B':
	cout<<B_s;
	break;
	case 'C':
	cout<<C_s;
	break;
	case 'D':
	cout<<D_s;
	break;
	default:
	cout<<"what?";
	break;
	}
	return 0;
}
