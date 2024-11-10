class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        std::map<int, int> mp;
        int operations = 0;
        std::map<int, int>::iterator it = mp.end();

        for (int i = 0; i < nums.size(); i++)
        {
            it = mp.find(k - nums[i]);
            if (it != mp.end())
            {
                if (it->second == 1)
                    mp.erase(it);
                else
                    it->second--;
                operations++;
            }
            else
                mp[nums[i]]++;
        }
        return operations;
    }
};