// 26. Remove Duplicates from Sorted Array

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
            int count = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            int currentdublicate = 0;
            if(nums[i] == val){
                currentdublicate = i;
                count++;
            }
            else if (nums[i] != val)
            {
                nums[currentdublicate] = nums[i];
                i = currentdublicate+1;
            }
            
        }
        return count;
    }
};
int main()
{

    vector<int> nums = {1,1,2};
        Solution s1;
       cout<< s1.removeElement(nums,1);

}
