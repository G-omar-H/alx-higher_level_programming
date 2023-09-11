#include "lists.h"
/**
 * aux_palind - check for match
 * @head: pointer to the first node
 * @end: pointer to the last node
 * Return: 1 if match , 0 (fails)
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to a pointer pointing to the first node
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}
