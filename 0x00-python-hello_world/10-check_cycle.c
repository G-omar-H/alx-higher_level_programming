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
	int i;

	current = list;
	for (i = 0; list != NULL && list->next != NULL && current->next->next != NULL; i++)
	{
		list = list->next;
		current = current->next->next;
		if (list == current)
			return (1);
	}
	return (0);
}
