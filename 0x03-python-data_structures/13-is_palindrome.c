#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *second_half, *prev_of_slow = NULL;
    int result = 1; // Assume it is a palindrome

    // If list is empty or has one element
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    // Find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_of_slow = slow;
        slow = slow->next;
    }

    // If the list has an odd number of elements, skip the middle element
    listint_t *middle = NULL;
    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    // Reverse the second half of the list
    second_half = reverse_list(slow);

    // Set the next of the middle node to the end of the reversed list
    if (middle != NULL)
        prev_of_slow->next = middle;
    else
        prev_of_slow->next = NULL;

    // Compare the first and second half
    listint_t *first_half = *head;
    while (second_half != NULL)
    {
        if (first_half->n != second_half->n)
        {
            result = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the original list (optional)
    // reverse_list(second_half); 
    // if (middle != NULL)
    //     prev_of_slow->next = middle;
    // else
    //     prev_of_slow->next = second_half;

    return result;
}
