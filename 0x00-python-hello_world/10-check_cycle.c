#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if for a lincked-list if it's cycle
 * @list: pointer to a node
 * Return: 1 if yes. 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *list1;
	int i;

	list1 = list;
	current = list1;
	for (i = 0; current != NULL && current->next->next != NULL; i++)
	{
		list1 = list1->next;
		current = current->next->next;
		if (list1->n == current->n)
			return (1);
	}
	return (0);
}
