#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - insert a node at a sorted position
 * @head: pointer to the first node
 * @number: value of the node to insert
 * Return: pointer to the new node, NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pos = NULL, *current = *head, *previous = *head;

	pos = malloc(sizeof(listint_t));
	pos->n = number;
	pos->next = NULL;

	if (current && number < current->n)
	{
		pos->next = *head;
		*head = pos;
		return (pos);
	}
	else if (current->next)
	{
		while (current && current->next)
		{
			current = current->next;
			if (current->n > number)
			{
				previous->next = pos;
				pos->next = current;
				return (pos);
			}
			previous = previous->next;
		}
	}
	free(pos);
	return (NULL);
}
