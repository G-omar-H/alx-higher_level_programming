#include "lists.h"
/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to a pointer pointing to the first node
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 1;
	listint_t *current = *head, *previous = *head;

	while (current)
	{
		current = current->next;
		i++;
	}
	if (i)
	{
		while (previous->next != NULL)
		{
			current = *head;
			for (j = 1; j < i; j++)
			{
				current = current->next;
			}
			if (previous->n != current->n)
				return (0);
			previous = previous->next;
			i--;
		}
	}
	return (1);
}
