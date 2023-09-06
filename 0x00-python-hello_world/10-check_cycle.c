#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if for a lincked-list if it's cycle
 * @list: pointer to a node
 * Return: 1 if yes. 0 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
