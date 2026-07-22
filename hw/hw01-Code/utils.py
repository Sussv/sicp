# **WARNING**
# This file does not contain problems.
# It only includes helper functions necessary for ok tests.
# There is no need to understand the contents of this file.
# Please do not modify this file.

import inspect
import ast
import re

def check_single_return(function):
    node_names = [type(x).__name__ for x in ast.parse(inspect.getsource(function)).body[0].body]
    if node_names != ['Expr', 'Return']:
        raise RuntimeError("Your code should consists of nothing but an return statement (and a doc string)")

def check_no_square_brackets(function):
    if len(re.findall(r'\[|\]', inspect.getsource(function), re.M)) != 0:
        raise RuntimeError("You should not use square brackets `[...]` in this problem")
