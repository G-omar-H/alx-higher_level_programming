#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number);
/**
 * insert_node - insert a node at a sorted position
 * @head: pointer to the first node
 * @number: value of the node to insert
 * Return: pointer to the new node, NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *pos = NULL;

	pos = malloc(sizeof(listint_t));
	if (!pos)
		return (NULL);
	pos->n = number;
	pos->next = NULL;

	current = *head;
	if (!current || pos->n < current->n)
	{
		pos->next = current;
		*head = pos;
		return (pos);
	}
	while (current)
	{
		if (!current->next || pos->n < current->next->n)
		{
			pos->next = current->next;
			current->next = pos;
			return (pos);
		}
		current = current->next;
	}
	free(pos);
	return (NULL);
}
