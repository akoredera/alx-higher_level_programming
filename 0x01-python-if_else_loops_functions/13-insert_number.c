#include "lists.h"
/**
 * insert_node - insert node
 * @head: address
 * @number: value
 * Return: address otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *temp;

	if (*head == NULL)
		return (NULL);
	current = *head;
	temp = NULL;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	while (current != NULL)
	{
		if (current->n > new->n)
		{
			new->next = current;
			current = temp;
			current->next = new;
			break;
		}
		temp = current;
		current = current->next;
	}
	return (new);
}
