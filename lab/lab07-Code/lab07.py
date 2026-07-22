""" Lab 07: Special Method, Linked Lists and Mutable Trees """

# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3

#####################
# Required Problems #
#####################

class Complex:
    """Complex Number.

    >>> a = Complex(1, 2)
    >>> a
    Complex(real=1, imaginary=2)
    >>> print(a)
    1 + 2i
    >>> b = Complex(-1, -2)
    >>> b
    Complex(real=-1, imaginary=-2)
    >>> print(b)
    -1 - 2i
    >>> print(a + b)
    0
    >>> print(a * b)
    3 - 4i
    >>> print(a)
    1 + 2i
    >>> print(b)
    -1 - 2i
    """
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __repr__(self):
        return 'Complex(real={0}, imaginary={1})'.format(self.real, self.imaginary)
    def __str__(self):
        if self.real == 0 and self.imaginary == 0:
            return '0'
        elif self.real == 0:
            return '{0}i'.format(self.imaginary)
        elif self.imaginary == 0:
            return '{0}'.format(self.real)
        elif self.imaginary < 0:
            return '{0} - {1}i'.format(self.real, -self.imaginary)
        else:
            return '{0} + {1}i'.format(self.real, self.imaginary)
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    def __mul__(self, other):
        return Complex((self.real * other.real - self.imaginary * other.imaginary), (self.real * other.imaginary + self.imaginary * other.real))
    
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(0)
    >>> s
    Link(0)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(8760)
    Link(8, Link(7, Link(6, Link(0))))
    """
    if n == 0:
        return Link(0)
    a = Link.empty
    while n != 0:
        t = n%10
        a = Link(t,a)
        n //= 10
    return a


def convert(link):
    """Convert a linked list to a Python list.

    >>> l = Link(Link(Link(1, Link(Link(2, Link(3)), Link(4))), Link(5)))
    >>> print(l)
    <<<1 <2 3> 4> 5>>
    >>> convert(l)
    [[[1, [2, 3], 4], 5]]
    >>> type(convert(l)) is list
    True
    """
    if link is Link.empty:
        return []
    if isinstance(link.first, Link):
        first = convert(link.first)
    else:
        first = link.first
    rest = convert(link.rest)
    return [first] + rest



def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    for branch in t.branches:
        cumulative_mul(branch)
        t.label *= branch.label  



def prune(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    for branch in t.branches:
        prune(branch, n)
    while len(t.branches) > n:
        max = 0
        max_label = t.branches[0].label
        for i in range(1, len(t.branches)):
            if t.branches[i].label > max_label:
                max_label = t.branches[i].label
                max = i
        t.branches.pop(max)


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
