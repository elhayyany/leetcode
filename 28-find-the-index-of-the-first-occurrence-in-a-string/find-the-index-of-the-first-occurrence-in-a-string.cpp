class Solution {
public:
    int strStr(string haystack, string needle) {
        int s = haystack.size() - needle.size() + 1;
        for (int i = 0; i < s; i++)
        {
            if (haystack[i] == needle[0])
            {
                int j = 0;
                for (; j < needle.size() && haystack[i] == needle[j]; j++, i++)
                {
                    if (j == needle.size() - 1) return (i - j);
                }
                i -= j;
            }
        }
        return -1;

    }
};