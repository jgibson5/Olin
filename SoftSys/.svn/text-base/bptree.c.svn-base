/* Example code for Software Systems at Olin College.

Copyright 2012 Allen Downey
License: Creative Commons Attribution-ShareAlike 3.0

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* The values in the B+ tree are just strings. */
typedef char * Value;

/* A Node can be either an interior node with children or a leaf with values */
typedef struct node {
    int is_leaf;
    int n;
    int keys[3];
    union {
	struct node *children[3];
	Value values[3];
    };
    struct node *next;
} Node;


/* Makes a new interior node. */
Node *make_node(int n, int *keys, Node **children) 
{
    Node *node = (Node *) malloc (sizeof (Node));
    node->n = n;
    node->is_leaf = 0;
    int i;
    for (i=0; i<n; i++) {
	node->keys[i] = keys[i];
	node->children[i] = children[i];
    }
    node->children[i] = children[i];
    return node;
}

/* Makes a new leaf node.  Allocates copies of the values. */
Node *make_leaf(int n, int *keys, Value *values) 
{
    Node *node = (Node *) malloc (sizeof (Node));
    node->n = n;
    node->is_leaf = 1;

    int i;
    for (i=0; i<n; i++) {
	node->keys[i] = keys[i];
	node->values[i] = strdup(values[i]);
    }
    return node;
}

/* Prints the keys in an interior node. */
void print_node (Node *node) 
{
    int i;
    for (i=0; i < node->n; i++) {
	printf("key %d\n", node->keys[i]);
    }
}

/* Prints the key-value pairs in a leaf node. */
void print_leaf (Node *node) 
{
    int i;
    for (i=0; i < node->n; i++) {
	printf("key %d val %s\n", node->keys[i], node->values[i]);
    }
}

/* Frees all nodes in the tree. */
void free_tree(Node *node) {
    int i;
    if (!node->is_leaf) {
	for (i=0; i < node->n; i++) {
	    free_tree(node->children[i]);
	}
    }
    free(node);
}

/* Removes a node from a B+ tree.

   If the child is a leaf node, it is also removed from
   the linked list.

   parent: must be an interior node.
   child_index: index of the child to be removed.
*/
Node *remove_node(Node *parent, int child_index)
{
    Node *child = parent->children[child_index];

    // shift over the remaining keys and children
    int i;
    for (i=child_index+1; i < parent->n; i++) {
	parent->keys[i-1] = parent->keys[i];
	parent->children[i-1] = parent->children[i];
    }
    // don't forget the extra child
    parent->children[i-1] = parent->children[i];
    parent->n -= 1;

    if (child_index == 0) return child;
    if (!child->is_leaf) return child;

    // remove the child node from the linked list
    Node *prev = parent->children[child_index-1];
    prev->next = child->next;

    return child;
} 

/* Prints all the values in order, one per line. */
void print_values(Node *node)
{
    // FIX ME!
}

/* Looks up a target key in a leaf node and returns the corresponding value.

   Returns NULL if the key is not in the node.
*/
Value leaf_lookup(Node *node, int target)
{
    // FIX ME!
    return NULL;
}

/* Looks up a target key in a B+ tree. */
Value lookup(Node *node, int target)
{
    // FIX ME!

    // first, find the correct leaf node
    // then call leaf_lookup to get the value

    return NULL;
}

int main ()
{
    int keys[] = {1, 2};
    char *values[] = {"one", "two"};

    Node *leaf1 = make_leaf(2, keys, (Value *) values);
    //print_leaf(leaf1);

    int keys2[] = {3, 4};
    char *values2[] = {"three", "four"};

    Node *leaf2 = make_leaf(2, keys2, (Value *) values2);
    //print_leaf(leaf2);

    int keys3[] = {5, 6, 7};
    char *values3[] = {"five", "six", "seven"};

    Node *leaf3 = make_leaf(3, keys3, (Value *) values3);
    //print_leaf(leaf3);

    leaf1->next = leaf2;
    leaf2->next = leaf3;
    leaf3->next = NULL;

    int keys4[] = {3, 5};
    Node *children[] = {leaf1, leaf2, leaf3};

    Node *root = make_node(2, keys4, children);
    // print_node(root);

    int key = 3;
    Value val = lookup(root, key);
    printf ("lookup: %d -> %s\n", key, val);
    // should print 3 -> three

    printf("values:\n");
    print_values(root);
    // should print "one two three four five six seven" (one per line)

    Node *removed = remove_node(root, 1);
    free_tree(removed);

    key = 7;
    val = lookup(root, key);
    printf ("lookup: %d -> %s\n", key, val);
    // should print 7 -> seven

    printf("values:\n");
    print_values(root);
    // should print "one two five six seven" (one per line)

    free_tree(root);

    return 0;
}
