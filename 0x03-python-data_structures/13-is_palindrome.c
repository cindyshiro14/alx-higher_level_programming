#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it's a palindrome, 0 if it's not
 */
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head;
listint_t *fast_ptr = *head;
listint_t *prev = NULL;
listint_t *mid = NULL;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (fast_ptr != NULL && fast_ptr->next != NULL)
{
fast_ptr = fast_ptr->next->next;
prev = slow_ptr;
slow_ptr = slow_ptr->next;
}

if (fast_ptr != NULL)
{
mid = slow_ptr;
slow_ptr = slow_ptr->next;
}

prev->next = NULL;
reverse_list(&slow_ptr);

is_palindrome = compare_lists(*head, slow_ptr);

if (mid != NULL)
{
prev->next = mid;
mid->next = slow_ptr;
}
else
{
prev->next = slow_ptr;
}

return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if lists are the same, 0 if not
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 != NULL && head2 != NULL)
{
if (head1->n != head2->n)
return (0);
head1 = head1->next;
head2 = head2->next;
}

if (head1 == NULL && head2 == NULL)
return (1);

return (0);
}
