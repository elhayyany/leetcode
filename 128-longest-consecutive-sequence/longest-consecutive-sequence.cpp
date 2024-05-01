class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_map<int, int> mp;
        int res = 0;
        for (int i: nums)
            mp[i] = 1;
        int j;
        std::unordered_map<int, int>::iterator tem;
        for (std::unordered_map<int, int>::iterator pr = mp.begin(); pr != mp.end(); pr++)
        {
            tem = mp.find(pr->first + 1);
            if (tem != mp.end())
            {
                j = tem->first;
                while (tem != mp.end())
                {
                    res += tem->second;
                    mp.erase(j);
                    j++;
                    tem = mp.find(j);
                }
            }
            pr->second += res;
            res = 0;
        }
        for (auto t: mp)
            if (t.second > res)
                res = t.second;
        return res;    
    }
};