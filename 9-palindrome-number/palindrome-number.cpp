class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        std::string num = to_string(x);
        for (int i = 0, j = num.size() - 1; i < j; i++, j--)
            if (num[i] != num[j]) return 0;
        return true;
    }
};