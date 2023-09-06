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
	listint_t *pos = NULL, *current = NULL, *previous = NULL;

	if (!head)
		return (NULL);
	pos = malloc(sizeof(listint_t));
	pos->n = number;
	pos->next = NULL;

	current = *head;
	previous = *head;
	if ((*head)->n > number)
	{

		pos->next = *head;
		*head = pos;
		return (pos);
	}
	else if (current->next)
	{
		while (current)
		{
			current = current->next;
			if (current->n > number)
			{
				previous->next = pos;
				pos->next = current;
				return (pos);
			}
			if (current)
				previous = previous->next;
		}
	}
	else if (previous->n < number)
	{
		previous->next = pos;
		pos->next = NULL;
		return (pos);
	}
	free(pos);
	return (NULL);
}
