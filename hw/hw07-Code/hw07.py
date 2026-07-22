""" Homework 07: Special Method, Linked Lists and Mutable Trees"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    
    def __init__(self, coefficients):
        if coefficients == [0] or coefficients == []:
            self.coefficients = [0]
        else:
            self.coefficients = coefficients
            while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
                self.coefficients.pop()


    def __repr__(self):
        return 'Polynomial(' + str(self.coefficients) + ')'
    

    '''def __str__(self):
        if self.coefficients == [0]:
            return '0'
        a = str(self.coefficients[0])
        for i, j in enumerate(self.coefficients):
            if i == 0:
                continue
            a += ' + '+str(j) + '*x^' + str(i)
        return a'''
    

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new = [0] * max_len
        for i, coeff in enumerate(self.coefficients):
            new[i] += coeff
        for j, coeff in enumerate(other.coefficients):
            new[j] += coeff
        return Polynomial(new)
    

    def __mul__(self, other):
        len1 = len(self.coefficients)
        len2 = len(other.coefficients)
        new = [0] * (len1 + len2 - 1)
        for i, coeff_a in enumerate(self.coefficients):
            for j, coeff_b in enumerate(other.coefficients):
                new[i + j] += coeff_a * coeff_b

        return Polynomial(new)
       
        


def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    
    if lnk is Link.empty:
        return
    current = lnk  
    while current.rest is not Link.empty:
        if current.first == current.rest.first:
            current.rest = current.rest.rest
        else:
            current = current.rest

def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    if lnk is Link.empty:
        return lnk
    prev = Link.empty
    current = lnk
    while current is not Link.empty:
        next = current.rest
        current.rest = prev
        prev = current
        current = next
    return prev
    
def rotate_right(lnk):
    """Rotate the linked list one step to the right.

    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> # Disallow creating new Links
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = rotate_right(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <4 1 2 3>
    >>> a.first   # Make sure original first not overwritten
    1
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    current = lnk
    while current.rest is not Link.empty:
        pre = current
        current = current.rest
    current.rest = lnk
    pre.rest = Link.empty
    return current


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self, other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        if self.label != other.label or len(self.branches) != len(other.branches):
            return False
        for i in range(len(self.branches)):
            if self.branches[i] != other.branches[i]:
                return False
        return True
            
        
        
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    def min(a, b):
        if a<b:
            return a
        else:
            return b
    def max(a, b):
        if a>b:
            return a
        else:
            return b
    def bst_min(t):
        if t.is_leaf():
            return t.label
        return min(t.label, bst_min(t.branches[0]))

    def bst_max(t):
        if t.is_leaf():
            return t.label
        if len(t.branches) == 1:
            return max(t.label, bst_max(t.branches[0]))
        return max(t.label, bst_max(t.branches[1]))

    if t.is_leaf():
        return True
    if len(t.branches) > 2:
        return False
    for branch in t.branches:
        if not is_bst(branch):
            return False
    if len(t.branches) == 1:
        min = bst_min(t.branches[0])
        max = bst_max(t.branches[0])
        return (max <= t.label) or (min > t.label)

    left, right = t.branches[0], t.branches[1]
    left_max = bst_max(left)
    right_min = bst_min(right)
    return left_max <= t.label and right_min > t.label


def count_coins(total, denominations):
    """
    Given a positive integer `total`, and a list of denominations,
    a group of coins make change for `total` if the sum of them is `total` 
    and each coin is an element in `denominations`.
    The function `count_coins` returns the number of such groups. 
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(total, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since there is no way to make change with empty denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    '''if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return None
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current'''
    if total == 0:
        return Tree("1")
    if total < 0 or len(denominations) == 0:
        return None
    without_tree = count_coins_tree(total, denominations[1:])
    with_tree = count_coins_tree(total - denominations[0], denominations)
    branches = []
    if without_tree is not None:
        branches.append(without_tree)
    if with_tree is not None:
        branches.append(with_tree)
    if not branches:
        return None
    current_label = "{0}, {1}".format(total, denominations)
    return Tree(current_label, branches)

##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    "*** YOUR CODE HERE ***"


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    "*** YOUR CODE HERE ***"


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
