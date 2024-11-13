#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &heights)
    {

        int firsthighest;
        int secondhighest;
        int left = 0;
        int right = heights.size() - 1;
        vector<int> areas = {};
        for (int i = 0; i < heights.size(); i++)
        {
            
            cout <<" pos "<< left << right << endl;
            areas.push_back(min(heights[left],heights[right])*abs(left-right));
            cout<<" area "<<min(heights[left],heights[right])*abs(left-right)<<"  ";
            
            if (heights[left] >= heights[right] && left < right)
            {

                right--;
            }
            else
            {
                left++;
            }

            //min(heights[left],heights[right])*abs(left-right);
            //areas.push_back(min(heights[left],heights[right])*abs(left-right));
        }

        int max =0;
        for (int i = 0; i < areas.size(); i++)
        {
            if(areas[i] > max){
                max = areas[i];
                cout<<" max "<<max;
            }
        }
        return max;
    }
};

int main()
{
    Solution s;
    vector<int> heights{4,2,2,1,1};
    cout << "  " << s.maxArea(heights);
}