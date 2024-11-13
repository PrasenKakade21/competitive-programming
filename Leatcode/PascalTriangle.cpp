// 26. Remove Duplicates from Sorted Array

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result{1};
        long prev = 1;
        for(int i = 1; i <= rowIndex; i++) {
             long next_val = prev * (rowIndex - i + 1) / i;
            result.push_back(next_val);
            prev = next_val;
        }
        for (int i = 0; i < result.size(); i++)
        {
            cout<<result[i]<<" ";
        }
        
        return result;
    }
};
int main()
{

    vector<int> nums = {1,1,2};
        Solution s1;
        int size;
        cin>>size;
        s1.getRow(size);
 

}