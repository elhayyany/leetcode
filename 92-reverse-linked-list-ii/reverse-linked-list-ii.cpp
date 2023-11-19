/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode    *save = head, *svd;
        ListNode    *lft, *posLeft, *rght;
       for (int i = 1; i < left - 1; i++)
            save = save->next;
        left == 1? lft = save : lft = save->next;
        svd = lft;
        posLeft = lft->next;
        right == left? rght = lft: rght = posLeft->next;
        while(posLeft && left < right)
        {
           posLeft->next = lft;
            lft = posLeft;
            posLeft = rght;
            rght? rght = rght->next: rght = rght;
            right--;
        }
        if (left == 1)
        {
            head = lft;
            save->next = posLeft;
        }
        else
        {
            save->next = lft;
            svd->next = posLeft;
        }
        return head;
    }
};