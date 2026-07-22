# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    >>> # You aren't expected to understand the code of this test.
    >>> # It's just here to check that definition of lambda_curry2 is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(lambda_curry2)).body[0].body]
    ['Expr', 'Return']
    """
    return lambda x: lambda y: func(x, y)


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def count(n):
        i ,total =1, 0
        while i <= n:
            if condition(n, i):
                total += 1
            i += 1
        return total
    return count


def sum(n, f):
    """
    Return the sum of the first n terms in the sequence defined by f.
    The terms to be summed are f(0), f(1), f(2), ..., f(n).

    >>> sum(5, lambda x: x * x)
    55
    >>> sum(3, lambda x: x + 1)
    10
    >>> sum(5, lambda x: 2**x)
    63
    """
    result = 0
    while n >= 0:
        result += f(n)
        n -= 1
    return result


def product(n, f):
    """
    Return the product of the first n terms in the sequence defined by f.
    The terms to be multiplied are f(0), f(1), f(2), ..., f(n).

    >>> product(4, lambda x: x)
    0
    >>> product(3, lambda x: x + 2)
    120
    >>> product(3, lambda x: x * x + 1)
    100
    """
    result = 1
    while n >= 0:
        result *= f(n)
        n -= 1
    return result


def trigger(n):
    """
    Return 0 if n is 0, and 1 otherwise.

    >>> trigger(0)
    0
    >>> trigger(4)
    1
    """
    if n == 0:
        return 0
    else:
        return 1


def product_of_trigger(n, f):
    """
    Return the product of trigger(f(0)), trigger(f(1)), trigger(f(2)), ..., trigger(f(n)).

    >>> product_of_trigger(0, lambda x: x * x - 9)
    1
    >>> product_of_trigger(1, lambda x: x * x - 9)
    1
    >>> product_of_trigger(2, lambda x: x * x - 9)
    1
    >>> product_of_trigger(3, lambda x: x * x - 9)
    0
    """
    return product(n,lambda k:trigger(f(k)))


def minimal_root(n, f):
    """
    Return the smallest k such that k is a root of f with 0 <= k <= n.
    If no such k exists, return n + 1

    >>> minimal_root(6, lambda x: x) # f(0) = 0
    0
    >>> minimal_root(6, lambda x: x * x - 5 * x + 6) # f(2) = 0, f(3) = 0
    2
    >>> minimal_root(6, lambda x: x * x + 1) # no roots
    7
    """
    return sum(n, lambda k: trigger(product_of_trigger(k, f)))
