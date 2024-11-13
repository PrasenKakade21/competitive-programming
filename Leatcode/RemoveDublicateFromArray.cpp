// 26. Remove Duplicates from Sorted Array

#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int count = 1;
        for (int i = 0; i < nums.size() - 1; i++)
        {
            int a = nums[i];
            int b = nums[i + 1];
            if (a == b)
            {
                nums.erase( nums.begin() +i );
                // cout<<(nums.begin() +i+1);
                i--;
            }
            else
            {
                count++;
            }
        }
        for (int i = 0; i < nums.size(); i++)
        {
        // cout<<nums[i]<<" ";
        }
        
        return count;
    }
};

int main()
{

    vector<int> nums = {1,1,2};
        Solution s1;
       cout<< s1.removeDuplicates(nums);

}