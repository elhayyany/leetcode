/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        if (!root)
            return NULL;
        if (!removeLeafNodes(root->left, target))
            root->left = NULL;
        if (!removeLeafNodes(root->right, target))
            root->right = NULL;
        if (!root->right && !root->left && root->val == target)
            return NULL;
        return root;
    }
};