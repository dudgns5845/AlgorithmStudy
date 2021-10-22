#include <iostream>
#include <list>

using namespace std;

list<int> input_list;
int main()
{
    cin.tie(NULL);
    cin.sync_with_stdio(false);
    
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        string message;
        cin >> message;
        
        if (message == "push")
        {
            int num;
            cin >> num;
            input_list.push_back(num);
        }
        if (message == "size")
        {
            cout << input_list.size() << "\n";
        }
        if (message == "empty")
        {
            if (input_list.empty())
            {

                cout << 1 << "\n";
            }
            else
            {
                cout << 0 << '\n';
            }
        }
        if (message == "pop")
        {
            if (input_list.empty())
            {
                cout << -1 << '\n';
            }
            else
            {
                cout << input_list.front() << "\n";
                input_list.pop_front();
            }
        }
        if (message == "front")
        {
            if (input_list.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << input_list.front() << "\n";
            }
        }
        if (message == "back") {
            if (input_list.empty())
            {
                cout << -1 << "\n";
            }
            else
            {
                cout << input_list.back() << "\n";
            }
        }
    }

    return 0;
}
