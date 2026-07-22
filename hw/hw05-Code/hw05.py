""" Homework 5: Nonlocal and Generators"""

from ADT import tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    a=[]
    def withdraw(amount,trypassword):
        nonlocal balance,a
        if len(a)==3:
           return "Your account is locked. Attempts: ['{0}', '{1}', '{2}']".format(a[0],a[1],a[2]) 
        if trypassword!=password:
            a.append(trypassword)
            return 'Incorrect password'
        else:
            if amount > balance:
                return 'Insufficient funds'
            balance=balance-amount
            return balance
    return withdraw


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    a=withdraw(0,old_pass)
    if type(a)==str:
        return a
    def joint_withdraw(amount,password):
        if password==new_pass:
            usedpassword=old_pass
        else:
            usedpassword=password
        return withdraw(amount,usedpassword)
    return joint_withdraw


def distribute_parfait(n, k):
    """Generates all distribution methods of the given number of parfaits n and positive number of members k. 
    each distribution method is a list of length k, indicating the number of parfaits each member receives.

    >>> methods = distribute_parfait(1, 1)
    >>> type(methods)
    <class 'generator'>
    >>> next(methods)
    [1]
    >>> try: #this piece of code prints "No more distribution methods!" if calling next would cause an error
    ...     next(methods)
    ... except StopIteration:
    ...     print('No more distribution methods!')
    No more distribution methods!
    >>> sorted(distribute_parfait(2, 2)) # Returns a sorted list containing elements of the generator
    [[1, 1]]
    >>> sorted(distribute_parfait(4, 3))
    [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    >>> sorted(distribute_parfait(5, 2))
    [[1, 4], [2, 3], [3, 2], [4, 1]]
    """
    if k==1:
        yield [n]
    else:
        for i in range(1,n-(k-1)+1):
            for j in distribute_parfait(n-i, k-1):
                yield [i]+j


def two_sum_pairs(target, pairs):
    """Return True if there is a pair in pairs that sum to target."""
    for i, j in pairs:
        if i + j == target:
            return True
    return False


def pairs(lst):
    """Yield the search space for two_sum_pairs.

    >>> two_sum_pairs(1, pairs([1, 3, 3, 4, 4]))
    False
    >>> two_sum_pairs(8, pairs([1, 3, 3, 4, 4]))
    True
    >>> lst = [1, 3, 3, 4, 4]
    >>> plst = pairs(lst)
    >>> n, pn = len(lst), len(list(plst))
    >>> n * (n - 1) / 2 == pn
    True
    """
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            yield lst[i],lst[j]


def two_sum_list(target, lst):
    """Return True if there are two different elements in lst that sum to target.

    >>> two_sum_list(1, [1, 3, 3, 4, 4])
    False
    >>> two_sum_list(8, [1, 3, 3, 4, 4])
    True
    """
    visited = []
    for val in lst:
        a=target-val
        if a in visited:
            return True
        visited.append(val)
    return False


def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> k = tree(5, [tree(7, [tree(2)]), tree(8, [tree(3), tree(4)]), tree(5, [tree(4), tree(2)])])
    >>> v = tree('Go', [tree('C', [tree('C')]), tree('A', [tree('S'), tree(6)]), tree('L', [tree(1), tree('A')])])
    >>> type(lookups(k, 4))
    <class 'generator'>
    >>> sorted([f(v) for f in lookups(k, 2)])
    ['A', 'C']
    >>> sorted([f(v) for f in lookups(k, 3)])
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    if label(k)==key:
        yield lambda v:label(v)
    for i,branch in enumerate(branches(k)):
        for lookup in lookups(branch,key):
            yield lambda v,j=i,l=lookup:l(branches(v)[j])
    
    


##########################
# Just for fun Questions #
##########################


def remainders_generator(m):
    """Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    0
    4
    8
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"


def starting_from(start):
    """Yields natural numbers starting from start.

    >>> sf = starting_from(0)
    >>> [next(sf) for _ in range(10)] == list(range(10))
    True
    """
    "*** YOUR CODE HERE ***"


def sieve(t):
    """Suppose the smallest number from t is p, sieves out all the
    numbers that can be divided by p (except p itself) and recursively
    sieves out all the multiples of the next smallest number from the
    reset of of the sequence.

    >>> list(sieve(iter([3, 4, 5, 6, 7, 8, 9])))
    [3, 4, 5, 7]
    >>> list(sieve(iter([2, 3, 4, 5, 6, 7, 8])))
    [2, 3, 5, 7]
    >>> list(sieve(iter([1, 2, 3, 4, 5])))
    [1]
    """
    "*** YOUR CODE HERE ***"

def primes():
    """Yields all the prime numbers.

    >>> p = primes()
    >>> [next(p) for _ in range(10)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    "*** YOUR CODE HERE ***"
