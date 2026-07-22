# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def factorial(n):
    """Return the factorial of a non-negative integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    
    if n==0:
        return 1
    else:
        return factorial(n-1)*n


def is_right_triangle(a, b, c):
    """Given three integers (maybe non-positive), judge whether the three
    integers can form the three sides of a right triangle.

    >>> is_right_triangle(2, 1, 3)
    False
    >>> is_right_triangle(5, -3, 4)
    False
    >>> is_right_triangle(5, 3, 4)
    True
    """
    if a<=0 or b<=0 or c<=0:
        return False
    elif a+b<=c or a+c<=b or b+c<=a:
        return False
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        return True
    else:
        return False
        
    


def number_of_k(n, k):
    """Return the number of occurrences of k in each digit of a non-negative
    integer n.

    >>> number_of_k(999, 9)
    3
    >>> number_of_k(1234321, 2)
    2
    """
    a=0
    if n==0 and k==0:
        return 1
    while n>0:
        if n%10==k:
            a=a+1
        n//=10
    return a
