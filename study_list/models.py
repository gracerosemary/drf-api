from django.db import models
from django.contrib.auth import get_user_model

class StudyList(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ARRAY = 'Arr'
    STACK = 'Stack'
    QUEUE = 'Queue'
    LINKED_LIST = 'LL'
    BINARY_TREE = 'BT'
    BINARY_SEARCH_TREE = 'BST'
    INSERTION_SORT = 'IS'
    MERGE_SORT = 'MS'
    QUICK_SORT = 'QS'
    structure_choices = (
        ('Arr', 'Array'),
        ('Stack', 'Stack'),
        ('Queue', 'Queue'),
        ('LL', 'Linked List'),
        ('BT', 'Binary Tree'),
        ('BST', 'Binary Search Tree'),
        ('HT', 'Hash Table'),
        ('IS', 'Insertion Sort'),
        ('MS', 'Merge Sort'),
        ('QS', 'Quick Sort'),
    )
    structure = models.CharField(
        max_length=20,
        choices=structure_choices,
        default=ARRAY,
    )

    SUM = 'Sum'
    VALUE_EXISTS = 'Value'
    FIND_DUPES = 'FD'
    REMOVE_DUPES = 'RD'
    REVERSE_VALUES = 'RV'
    MAX_VALUE = 'Max'
    MIN_VALUE = 'Min'
    SORT_VALUES = 'Sort'
    IMPLEMENTATION = 'Imp'
    DEFINE_STRUCTURE = 'Def'
    action_choices = (
        ('Sum', 'Find the sum of all elements'),
        ('Value', 'If the value is present, return True'),
        ('FD', 'Return a list of duplicate values'),
        ('RD', 'Remove all duplicate values'),
        ('RV', 'Reverse the values'),
        ('Max', 'Find the max value'),
        ('Min', 'Find the min value'),
        ('Sort', 'Sort the values'),
        ('Imp', 'Implement data structure'),
        ('Def', 'Define the general algorithm in your own words'),
    )
    action = models.CharField(
        max_length=64,
        choices=action_choices,
        default=DEFINE_STRUCTURE,
    )

    RECURSIVE = 'REC'
    ITERATIVE = 'IT'
    NA = 'NA'
    method_choices = (
        ('REC', 'Recursive'),
        ('IT', 'Iterative'),
        ('NA', 'Not Applicable')
    )
    method = models.CharField(
        max_length=20,
        choices=method_choices,
        default=NA,
    )

    notes = models.TextField()

    def __str__(self):
        return self.structure