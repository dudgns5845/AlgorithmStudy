#include<iostream>
#include<list>

using namespace std;

int main() {

    list<int> input_list;
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        input_list.push_front(i);
    }

    while (input_list.size() > 1) {
    
        input_list.pop_back();
        int temp = input_list.back();
        input_list.pop_back();
        input_list.push_front(temp);
        
    }

    cout << input_list.back();
    return 0;
}