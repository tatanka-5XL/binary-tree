# binary_tree.py

import sys

class Binary_object:
    '''
    Define basic object of a binary tree
    '''

    def __init__(self, number, left, right):
        self.number = number
        self.left = left
        self.right = right

    def give_number(self):
        return

    def give_left(self):
        return self.left

    def give_right(self):
        return self.right


def generate_tree():
    '''
    Generate binary tree to test the search function
    '''
    tree = []
    for i in (n+1 for n in range(32)):
        bo = Binary_object(i, 2 * i + 1, 2 * i)
        tree.append(bo)
    return tree


def input_object(number):
    while True:
        try:
            input_object = int(input(f'Provide object number {number}: '))
            assert (input_object > 1) and (input_object < 32)
            break
        except:
            print('Please, provide a whole number between 2 and 31: ')
    return input_object


def get_numbers_before(object):
    numbers_before = set()
    for i in range(1, object):
        numbers_before.add(i)
    return numbers_before


def get_direct_parent(tree, object):
    numbers_before = get_numbers_before(object)
    lefts_before = {}
    rights_before = {}
    for number in numbers_before:
        lefts_before[tree[number-1].number] = tree[number-1].left
    for number in numbers_before:
        rights_before[tree[number-1].number] = tree[number-1].right

    if object in lefts_before.values():
        for number, left in lefts_before.items():
            if left == object:
                return number
    else:
        for number, right in rights_before.items():
            if right == object:
                return number

def main():
    """
    Find first common parent object of two different objects in a binary tree!
    """
    tree = generate_tree()

    print("""
        Imagine a binary tree with objects from 1 to 32, arranged in rows from left to right, like follows:
                           1
                       /      \\
                     2           3
                   /   \\       /   \\
                  4     5     6      7
        ...etc.

        Provide two objects to calculate their first common parent!

        """)
    orig_input1 = input_object(1)
    while True:
        try:
            orig_input2 = input_object(2)
            assert orig_input2 != orig_input1
            break
        except:
            print('The numbers must be different!')

    input1 = orig_input1
    input2 = orig_input2

    while (input1 != input2):
        if input1 > input2:
            input1 = get_direct_parent(tree, input1)
        else:
            input2 = get_direct_parent(tree, input2)

    print(f'The highest common parent of numbers {orig_input1} and {orig_input2} in a binary tree is number {input1}.')
    return input1

main()
