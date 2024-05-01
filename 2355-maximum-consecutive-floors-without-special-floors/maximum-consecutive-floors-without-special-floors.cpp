class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        int res = 0;
        int max = 0;

        sort(special.begin(), special.end());
        max = special[0] - bottom;
        for (int i = 1; i < special.size(); i++)
        {
            if (max < special[i] - special[i-1] - 1)
                max = special[i] - special[i-1] - 1;
        }
        if (max < top - special[special.size() - 1])
            return top - special[special.size() - 1];
        return max;
    }
};