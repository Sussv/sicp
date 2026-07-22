"""Homework 4: Data Abstraction and Trees"""

from copy import deepcopy
from ADT import tree, label, branches, is_leaf, print_tree, copy_tree

#####################
# Required Problems #
#####################


# Problem 1.1
def fn_empty():
    """Return an empty function.

    >>> fn_empty()
    []
    """
    return []


def fn_remap(fn, x, y):
    """Return a new function that is the same as fn except that it maps x to y.

    >>> f = fn_remap(fn_empty(), 1, 2)
    >>> f
    [[1, 2]]
    >>> fn_remap(f, 1, 3)
    [[1, 3]]
    >>> fn_remap(f, 2, 3)
    [[1, 2], [2, 3]]
    """
    a=[]
    for i,j in fn:
        if i==x:
            a+=[[i,y]]
        else:
            a+=[[i,j]]
    if [x,y] not in a:
        a+=[[x,y]]
    return a


def fn_domain(fn):
    """Return a sorted list of all the inputs (domain) of fn.
    Note that if fn maps x to None, then x is not in the domain of fn.

    >>> fn_domain(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3))
    [1, 2]
    >>> fn_domain(fn_remap(fn_remap(fn_empty(), 2, 3), 1, 2))
    [1, 2]
    >>> fn_domain(fn_empty())
    []
    >>> fn_domain(fn_remap(fn_empty(), 1, None))
    []
    """
    a=[]
    for i,j in fn:
        if j is not None:
            a+=[i]
    a=sorted(a)
    return a

def fn_call(fn, x):
    """Return the result of applying fn to x.
    If fn does not map x to a value, return None.

    >>> fn_call(fn_remap(fn_empty(), 1, 2), 1)
    2
    >>> fn_call(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3), 2)
    3
    >>> fn_call(fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3), 1)
    2
    >>> fn_call(fn_empty(), 1) is None
    True
    """
    for i in fn:
        if i[0]==x:
            return i[1]


# Problem 1.2
def fn_ext(fn1, fn2):
    """Return whether fn1 and fn2 represent the same function.
    Two functions are the same if and only if they have the same domain
    and output the same value for each input in the domain.

    >>> f = fn_remap(fn_empty(), 1, 2)
    >>> g = fn_remap(fn_empty(), 2, 3)
    >>> fn_ext(f, g)
    False
    >>> fn_ext(fn_remap(f, 2, 3), g)
    False
    >>> fn_ext(fn_remap(f, 2, 3), fn_remap(g, 1, 2))
    True
    """
    if fn_domain(fn1)==fn_domain(fn2):
        for i in fn_domain(fn1):
            if fn_call(fn1, i)!=fn_call(fn2, i):
                return False
        return True
    return False


def fn_compose(fn1, fn2):
    """Return a new function that is the composition of fn1 and fn2.
    The composition of two functions fn1 and fn2 is a function fn such that
    fn(x) = fn1(fn2(x)) for every x in the domain of fn2.

    >>> f = fn_remap(fn_empty(), 2, 3)
    >>> g = fn_remap(fn_empty(), 1, 2)
    >>> h = fn_compose(f, g)
    >>> fn_call(h, 1)
    3
    >>> fn_call(h, 2) is None
    True
    """
    a=fn_empty()
    for i in fn_domain(fn2):
        if fn_call(fn1, fn_call(fn2, i)) is not None:
            a=fn_remap(a,i,fn_call(fn1, fn_call(fn2, i)))
    return a
    

def fn_inverse(fn):
    """Return a new function that is the inverse of fn.
    The inverse of a function fn is a function fn_inv such that
    fn_inv(y) = x if and only if fn(x) = y.
    If fn is not invertible, return None.

    >>> f = fn_remap(fn_remap(fn_empty(), 1, 2), 2, 3)
    >>> fn_call(fn_inverse(f), 3)
    2
    >>> g = fn_remap(fn_remap(fn_empty(), 1, 2), 2, 2)
    >>> fn_inverse(g) is None
    True
    """
    a,b=fn_empty(),[]
    for i in fn_domain(fn):
        if fn_call(fn,i) in b:
            return None
        a=fn_remap(a,fn_call(fn,i),i)
        b=fn_domain(a)
    return a
    

# Problem 2.1
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    t=[]
    branches1=branches(t1)
    branches2=branches(t2)
    newlabel=label(t1)+label(t2)
    a=max(len(branches1),len(branches2))
    for i in range(a): 
        p=branches1[i] if i<len(branches1) else None
        q=branches2[i] if i<len(branches2) else None
        if p is not None and q is not None:
            t.append(add_trees(p, q))
        elif p is not None:
            t.append(copy_tree(p))
        elif q is not None:
            t.append(copy_tree(q))
        else:
            t.append()
    return tree(newlabel,t)



# Problem 2.2
def bigpath(t, n):
    """Return the number of rooted paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    def f(sum,s):
        count=0
        sum+=label(s)
        if sum>=n:
            count+=1
        for i in branches(s):
            count+=f(sum, i)
        return count
    return f(0,t)



# Problem 2.3
def bigger_path(t, n):
    """Return the number of general rooted paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    sum=bigpath(t, n)
    for i in branches(t):
        sum+=bigger_path(i,n)
    return sum

# Problem 2.4
def has_path(t, word):
    """Return whether there is a rooted path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, "no path for empty word."
    def f(nowword,t):
        nowword+=label(t)
        if nowword==word:
            return True
        else:
            for i in branches(t):
                if f(nowword,i):
                    return True
            return False
    return f('',t)

##########################
# Just for fun Questions #
##########################


# Problem 3
def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    if is_leaf(t):
        return base_func(label(t))
    return merge_func(label(t),[fold_tree(b, base_func, merge_func) for b in branches(t)])

def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, lambda x:1, lambda x,y:sum(y))


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, lambda x:x, lambda x,y:x+sum(y))


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, "YOUR EXPRESSION HERE", "YOUR EXPRESSION HERE")


def has_path_fold(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path_fold(greetings, 'h')
    True
    >>> has_path_fold(greetings, 'i')
    False
    >>> has_path_fold(greetings, 'hi')
    True
    >>> has_path_fold(greetings, 'hello')
    True
    >>> has_path_fold(greetings, 'hey')
    True
    >>> has_path_fold(greetings, 'bye')
    False
    """
    assert len(word) > 0, "no path for empty word."

    def base_func(l):
        return "YOUR EXPRESSION HERE"
    def merge_func(l, bs):
        return "YOUR EXPRESSION HERE"

    return fold_tree(t, base_func, merge_func)(word)
