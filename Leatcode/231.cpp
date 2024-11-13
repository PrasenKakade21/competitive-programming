#include<math.h>
class Solution
{
public:
    bool isPowerOfTwo(int n)
    {
        if (n % 2 != 0 && n != 1)
        {
            return false;
        }
        else
        {
            int i = 0;
            while ( pow(2,i)<= n)
            {
                if (pow(2,i) == n)
                {
                    return true;
                }
                else
                {
                    i++;
                }
            }
        }
                return false;
    }
};