#include <vector>
#include <iostream>
using namespace std;


class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        
                vector<int> result(2);
          
        for(int x = 0 ;x <nums.size();x++){
            
            for(int y = nums.size()-1 ;y <nums.size();y--){
                
            if(abs(x - y) >= indexDifference && abs(nums[x] - nums[y]) >= valueDifference){

                result[0] = x;
                result[1] = y;
                return result;
            }
        } 
        }
              result[0] = -1;
                result[1] = -1;
            return result;
  
    }
};

int main()
{
    string str1, str2;
    str2 = "abcde";
    str1 = "(){}}{";
    Solution s;
    cout << s.isValid(str1);
    [5,1,4,1]
2
4
}
