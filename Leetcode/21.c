/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2)
{
    struct ListNode *l3;
    struct ListNode *p1 = l1;
    struct ListNode *p2 = l2;
    struct ListNode *pnewnode;

    if (NULL == l1)
        return l2;
    if (NULL == l2)
        return l1;
    if (l1->val >= l2->val)
    {
        l3 = l2;
        p2 = p2->next;
    }
    else
    {
        l3 = l1;
        p1 = p1->next;
    }
    pnewnode = l3;
    while (p1 && p2)
    {
        if (p1->val <= p2->val)
        {
            pnewnode->next = p1;
            pnewnode = p1;
            p1 = p1->next;
        }
        else
        {
            pnewnode->next = p2;
            pnewnode = p2;
            p2 = p2->next;
        }
    }
    if (!p1)
    {
        pnewnode->next = p2;
    }
    if (!p2)
    {
        pnewnode->next = p1;
    }
    return l3;
}