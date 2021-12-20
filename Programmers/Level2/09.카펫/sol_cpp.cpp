#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow)
{
    vector<int> answer;

    int size = brown + yellow;

    for (int row = 3; row < brown; row++)
    {

        if (size % row != 0)
            continue;

        int col = size / row;
        if ((col - 2) * (row - 2) == yellow)
        {
            answer.push_back(col);
            answer.push_back(row);
            break;
        }
    }
    return answer;
}