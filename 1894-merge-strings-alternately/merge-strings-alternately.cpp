class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int w1l = word1.length();
        int w2l = word2.length();
        string a(w1l + w2l, 'x');
        int i = 0;
        while (word1[int(i/2)] && word2[int(i/2)])
        {
            a[i] = word1[int(i/2)];
            i++;
            a[i] = word2[int(i / 2)];
            i++;
        }
        while (w1l < w2l)
            a[i++] = word2[w1l++];
        while (w1l > w2l)
            a[i++] = word1[w2l++];
        return a;
    }
};