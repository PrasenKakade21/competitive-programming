#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        int slen = s.size();

        if (slen == t.size())
        {

            for (int i = slen - 1; i > -1; i--)
            {
                for (int j = t.size() - 1; j > -1; j--)
                {
                    if (s[i] == t[j])
                    {

                        t.pop_back();
                    }
                }
                if (s.size() == t.size())
                {
                    return false;
                }
            }
        }
        if (t.size() == 0)
        {
            return true;
        }
        return false;
    }
};

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() == t.size())
        {

            for (int i = 0; i < s.size(); i++)
            {
                for (int j = i; j < s.size(); j++)
                {
                    if (s[i] > s[j])
                    {
                        char temp = s[i];
                        s[i] = s[j];
                        s[j] = s[temp];
                        cout<<s[j]<<s[temp];
                    }
                    if (t[i] > t[j])
                    {
                        char temp = t[i];
                        t[i] = t[j];
                        t[j] = t[temp];
                    }
                }
            }

            if (s == t)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
        return false;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        map<char,int> occuranceS;
        map<char,int> occuranceT;
        for (int i = 0; i < s.size(); i++)
        {
            occuranceS[s[i]] = occuranceS.at(s[i]) +1; 
            occuranceT[t[i]] = occuranceT.at(t[i]) +1; 

        }
        return occuranceS == occuranceT;

        

    }
};