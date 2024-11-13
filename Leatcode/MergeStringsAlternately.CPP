#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string merged = "";
        int lena, lenb;
        lena = word1.size();
        lenb = word2.size();
        int i = 0;

        for (i;i < min(lena, lenb); i++)
        {
            if (lena >= i)
            {
                merged.push_back(word1[i]);
            }
            if (lenb >= i)
            {
                merged.push_back(word2[i]);
            }
        }
        if (lena > lenb)
        {
            for (i;i < lena; i++)
            {
                merged.push_back(word1[i]);
            }
        }
        else{
             for (i;i < lenb; i++)
            {
                merged.push_back(word2[i]);
            }
        }
        cout<<merged;
        return merged;
    }
};

int main()
{
    string str1, str2;
    str2 = "abcde";
    str1 = "xyz";
    Solution s;
    s.mergeAlternately(str1, str2);
}
