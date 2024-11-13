#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    vector<vector<int>> generate(int numRows) {

        vector<vector<int>> result;
        for (size_t i = 0; i < numRows; i++)
        {
        vector<int> res(1, 1);
        long long prev = 1;
        for(int k = 1; k <= i; k++) {
            long long next_val = prev * (i - k + 1) / k;
            res.push_back(next_val);
            prev = next_val;
        }
        result.push_back(res);
        }
        return result;
    }
};