#include <string>
#include <iostream>
#include <stack>
using namespace std;
class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> paranthesis;
        if (s[0] == ')' || s[0] == ']' || s[0] == '}')
            return false;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
                paranthesis.push(s[i]);
            else if (paranthesis.size())
            {
                char c = paranthesis.top();
                if (c == '(' && s[i] != ')')
                    return false;
                else if (c == '[' && s[i] != ']')
                    return false;
                else if (c == '{' && s[i] != '}')
                    return false;
                paranthesis.pop();
            }
            else
                return false;
        }
        if (!paranthesis.empty())
            return false;
        return true;
    }
};
int main()
{
    string str1, str2;
    str2 = "abcde";
    str1 = "(){}}{";
    Solution s;
    cout << s.isValid(str1);
}
