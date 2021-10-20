#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(pair<int, string> a, pair<int, string>b) {
    if (a.first == b.first) {
        return a.second < b.second;
    }
    return a.first < b.first;
}

int main()
{
    int N;
    cin >> N;

    vector<pair<int, string>> input_list;

    for (int i = 0; i < N; i++)
    {
        string input_text;
        cin >> input_text;
        input_list.push_back(make_pair(input_text.length(), input_text));
    }
    sort(input_list.begin(), input_list.end(), compare);
    input_list.erase(unique(input_list.begin(), input_list.end()),input_list.end());
    
    for (int i = 0; i < input_list.size(); i++) {
        cout << input_list[i].second << '\n';
    }
    return 0;
}