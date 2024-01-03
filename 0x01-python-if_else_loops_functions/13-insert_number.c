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

	if (*head == NULL)
		return (NULL);
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = current->next;
	current->next = new;
	return (new);
}
