#include <string>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> result(2);
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            for (int j = i + 1; j < nums.size() - 1; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    result[0] = nums[i];
                    result[1] = nums[j];
                    return result;
                }
            }
        }
    }
};
int main()
{
    vector<int> str1, str2;
    str1 = {1, 2, 3, 4, 5};
    Solution s;
    str2 = s.twoSum(str1, 8);
    cout << str2[0]<< " " << str2[1];
}
