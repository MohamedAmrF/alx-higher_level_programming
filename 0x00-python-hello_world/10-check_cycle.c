#include "lists.h"

/**
* check_cycle - checks for a cycle in a linked list
* @list: the pointer to the beginning of the list
*
* Return: 1 if a cycle is found, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *slow = head, *fast = head;

	if (head == NULL)
		return (0);
	while (1)
	{
		if (slow->next == NULL)
			return (0);
		slow = slow->next;

		if (fast->next == NULL)
			return (0);
		fast = fast->next;
		if (fast->next == NULL)
			return (0);
		fast = fast->next;

		if (fast == slow)
			return (1);
	}
}
