// 35. Search Insert Position

#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        vector<int> result = binarySearch(nums, 0, nums.size() - 1, target);
        if (result[0] != -1)
        {
            return result[0];
        }
        else
        {
            return result[1];
        }
    }
    vector<int> binarySearch(vector<int> &nums, int l, int r, int t)
    {
        vector<int> result;
        while (l <= r)
        {
            int m = l + (r - l) / 2;

            if (nums[m] == t)
            {

                result[0] = m;
                return result;
            }

            if (nums[m] < t)
            {
                result[1] = m;
                l = m + 1;
            }

            else
                r = m - 1;
        }
        result[0] = -1;
        return result;
    }
};

int main()
{
    vector<int> nums = {1, 1, 2};
    Solution s1;
    cout << s1.searchInsert(nums, 2);
}
