#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string result;
        for (int i = 0; i < strs.size(); i++)
        {
            string s = strs[i];
            if (i == 0)
            {
                result = s;
            }
            else
            {
                int j = 0;
                while (j <= min(result.size(), s.size()))
                {
                    if (result[j] == s[j])
                    {
                        j++;
                    }
                    else
                    {
                        if (j == 0)
                        {
                            return "";
                        }
                        result.erase(result.begin() + j, result.end());
                        if (result.size() == 0)
                        {
                            return "";
                        }
                        break;
                    }
                }
            }
        }
        return result;
    }
};

int main()
{

    vector<string> lis{"ab", "a"};
    string st = "ab";
    Solution s;

    cout << s.longestCommonPrefix(lis) << endl;
}