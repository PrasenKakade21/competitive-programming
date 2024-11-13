// 66. Plus One

// 35. Search Insert Position

#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int remainder = 1;
        for (int i = digits.size() - 1; i >= 0; i--)
        {
            int temp = digits[i] + remainder;
            digits[i] = temp % 10;
            remainder = temp / 10;
        }
        if (remainder != 0)
            digits.insert(digits.begin(), remainder);
        return digits;
    }
};
class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        digits.erase(digits.begin());

        int len = digits.size();
        int i = len - 1;
        while (i > -1)
        {
            if (i = len - 1)
            {
                digits[i]++;
            }
            if (i == 0 && digits[i] == 10)
            {
                digits[i] = 0;
                digits.insert(digits.begin(), 1);
            }
            else if (digits[i] == 10)
                digits[i] = 0;
            else
                break;
            i--;
        }
        return digits;
    }
};

int main()
{
    vector<int> nums = {1, 2, 3, 4};
    Solution s1;
    vector<int> digits = s1.plusOne(nums);

    for (int i = 0; i < digits.size(); i++)
    {
        cout << digits[i] << " ";
    }
}
