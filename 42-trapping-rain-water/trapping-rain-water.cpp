class Solution {
public:
    int trap(vector<int>& height) {
        int first = 0;
        int res = 0;
        for(int i = 1; i < height.size() - 1; i++)
        {
            if (height[i] < height[first])
            {
                res += height[first] - height[i];
            }
            else
                first = i;
        }
        if (height[height.size() - 1] < height[first])
        {
            int loc = height[height.size() - 1];
            for (int i = height.size() - 2; i > first && loc < height[first]; i--)
            {
                if (height[i] >= loc)
                    loc = height[i];
                res -= height[first] - loc;
            }
        }
        return (res);
    }
};
