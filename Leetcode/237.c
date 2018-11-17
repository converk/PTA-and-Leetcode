/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

//删除链表中的节点
void deleteNode(struct ListNode *node)
{
    struct ListNode *P = node->next;
    node->val = P->val;
    node->next = P->next;
}