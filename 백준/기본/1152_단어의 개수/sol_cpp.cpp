#include <iostream>
#include <string>
using namespace std;

int main()
{
    string input_text;
    getline(cin, input_text);
    if (input_text.empty())
    {
        cout << "0";
        return 0;
    }
    int count_word = 0;
    for (int i = 0; i < input_text.length(); i++)
    {
        if (input_text[i] == ' ')
        {
            if (i == 0 || i == input_text.length() - 1)
            {
                continue;
            }
            else
            {
                count_word++;
            }
        }
    }
    if (input_text.length() == 1 && input_text[0] == ' ')
    {
        cout << "0";
        return 0;
    }
    else
    {
        cout << count_word + 1;
        return 0;
    }
}