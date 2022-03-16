#include <iostream>
#include <string>
#include <vector>
using namespace std;

//월별 일수 
int Days[13] = { 0,31,28,31,30,31,30,31,31,30,31,30,31 };
//일별 금액 저장하는 곳
int moneyRecord [366] = { 0, };
int B, S, G, P, D;

void ParseInput(string input) {
	
	int month = stoi(input.substr(5, 2));
	int day = stoi(input.substr(8, 2));
	int money = stoi(input.substr(11));

	int index = 0; 
	for (int i = 1; i < month; i++) {
		index += Days[i];
	}
	index += day;
	
	for (int i = 0; i < 30; i++) {
		if (index + i >= 366) return;
		moneyRecord[index + i] += money;
	}

	

}

void checkLevel() {
	for (int i = 1; i < 366; i++) {
		if (0 <= moneyRecord[i] && moneyRecord[i] < 10000) B++;
		else if (10000 <= moneyRecord[i] && moneyRecord[i] < 20000) S++;
		else if (20000 <= moneyRecord[i] && moneyRecord[i] < 50000) G++;
		else if (50000 <= moneyRecord[i] && moneyRecord[i] < 100000) P++;
		else if (100000 <= moneyRecord[i]) D++;
	}
}

int main() {
	
	ParseInput("2019/12/30 5000");
	
	checkLevel();

	for (int i = 1; i < 366; i++) {
		if (i % 10 == 0) cout << endl;
		cout << moneyRecord[i] << " ";
	}
	
}