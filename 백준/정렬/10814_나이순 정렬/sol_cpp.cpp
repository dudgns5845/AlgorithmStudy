#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, string> a, pair<int, string> b) {
    //나이가 같으면 입력받은 순서대로
    if (a == b) {
        return false;
    }
    return a.first < b.first;
}

int main() {

    int N;
    cin >> N;

    vector<pair<int, string>> input_list;
    for (int i = 0; i < N; i++) {
        int age;
        string name;
        cin >> age >> name;
        input_list.push_back(make_pair(age, name));
    }

    // 안정 정렬
    stable_sort(input_list.begin(), input_list.end(),compare);

    for (int i = 0; i < input_list.size(); i++) {
        cout << input_list[i].first << " " << input_list[i].second << '\n';
   }
    return 0;
}