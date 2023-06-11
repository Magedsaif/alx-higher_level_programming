#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: address of the new element or NULL if it fails
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;

	if (!head || !*head || !(*head)->next)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
