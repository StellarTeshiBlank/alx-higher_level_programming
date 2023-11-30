#include "lists.h"

/**
 * insert_node - inserts a new node at a given position in a sorted list.
 * @head: pointer to the head of the list.
 * @number: value of the new node.
 * Return: the address of the new node, or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	prev = *head;
	current = (*head)->next;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new->next = current;
	prev->next = new;

	return (new);
}
