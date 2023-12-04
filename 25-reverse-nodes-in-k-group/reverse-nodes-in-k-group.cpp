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
    int getGroupNums(ListNode* head, int k)
    {
        int i = 0;
        while (head)
        {
            i++;
            head = head->next;
        }
        return int(i/k);
    }
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int         groupNums, edgeNums;
        ListNode    *groupTail;
        ListNode    *groupHead;
        ListNode    *node, *next, *postNext;
        bool        first = true;
        groupNums = getGroupNums(head, k);
        groupTail = head->next;
        node = head;
        next = head->next;
        postNext = next ? next->next : NULL;
        while(groupNums)
        {
            edgeNums = k - 1;
            groupHead = node;
            while (edgeNums)
            {
                next->next = node;
                node = next;
                next = postNext;
                postNext = postNext ? postNext->next:NULL;
                edgeNums--;
            }
            if (first)
            {
                head = node;
                first = 0;
            }
            else
                groupTail->next = node;
            node = next;
            next = postNext;
            postNext = next?next->next:NULL;
            groupTail = groupHead;
            groupNums--;
        }
        groupHead->next = node;
        return head;
    }
};