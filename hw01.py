"""Question 1 I could not access Syllabus Quiz"""

"""Question 2"""

# from operator import add, sub
# def a_plus_abs_b(a, b):
#     """Return a+abs(b), but without calling abs.

#     >>> a_plus_abs_b(2, 3)
#     5
#     >>> a_plus_abs_b(2, -3)
#     5
#     >>> # a check that you didn't change the return statement!
#     >>> import inspect, re
#     >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
#     ['return h(a, b)']
#     """
#     if b >= 0:
#         h = add
#     else:
#         h = sub
#     return h(a, b)


# print(a_plus_abs_b(2, 3))
# print(a_plus_abs_b(2, -3))

# """Q3: Two of Three"""


# def two_of_three(x, y, z):
#     """Return a*a + b*b, where a and b are the two smallest members of the
#     positive numbers x, y, and z.

#     >>> two_of_three(1, 2, 3)
#     5
#     >>> two_of_three(5, 3, 1)
#     10
#     >>> two_of_three(10, 2, 8)
#     68
#     >>> two_of_three(5, 5, 5)
#     50
#     >>> # check that your code consists of nothing but an expression (this docstring)
#     >>> # a return statement
#     >>> import inspect, ast
#     >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
#     ['Expr', 'Return']
#     """
#     return min(x*x + y*y, y*y + z*z, z*z + x*x)


# print(two_of_three(5, 5, 5))


# """Q4: Largest Factor"""


# def largest_factor(n):
#     """Return the largest factor of n that is smaller than n.

#     >>> largest_factor(15) # factors are 1, 3, 5
#     5
#     >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
#     40
#     >>> largest_factor(13) # factor is 1 since 13 is prime
#     1
#     """
#     d = n - 1
#     while d > 0:
#         if n % d == 0:
#             return d
#         d -= 1


# print(largest_factor(15))


# def largest_factor(n):  # call expression
#     """Return the largest factor of n that is smaller than n.

#     >>> largest_factor(15) # factors are 1, 3, 5
#     5
#     >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
#     40
#     >>> largest_factor(13) # factor is 1 since 13 is prime
#     1
#     """
#     d = n - 1  # 14
#     while d > 0:  # 14 greater than zero
#         if n % d == 0:  # if the reaminder of N % D equals 0 then return D
#             return d
#         d -= 1


# print(largest_factor(15))

# # ''''Q5: If Function vs Statement'''

# def if_function(condition, true_result, false_result):
#     """Return true_result if condition is a true value, and
#     false_result otherwise.

#     >>> if_function(True, 2, 3)
#     2
#     >>> if_function(False, 2, 3)
#     3
#     >>> if_function(3==2, 3+2, 3-2)
#     1
#     >>> if_function(3>2, 3+2, 3-2)
#     5
#     """
#     if condition:
#         return true_result
#     else:
#         return false_result


# def with_if_statement():
#     """
#     >>> result = with_if_statement()
#     47
#     >>> print(result)
#     None
#     """
#     if cond():
#         return true_func()  # 42
#     else:
#         return false_func()  # 47


# def with_if_function():
#     """
#     >>> result = with_if_function()
#     42
#     47
#     >>> print(result)
#     None
#     """
#     return if_function(cond(), true_func(), false_func())


# def cond():
#     return False


# def true_func():
#     print(42)


# def false_func():
#     print(47)


# from operator import add, mul  # adding these functions so I can run mul * 3 and then add + 1
# def hailstone(x):
#     """Print the hailstone sequence starting at x and return its
#     length.
#     >>> a = hailstone(10)
#     10
#     5
#     16
#     8
#     4
#     2
#     1
#     >>> a
#     7
#     """
#     count = 1
#     print(x)  # this is printing hailstone sequence starting at N, N =10
#     while x > 1:
#         if x % 2 == 0:  # 10 % 2 = 0
#             x = x // 2  # On first round this would result in 5, then we go into else statement
#         else:
#             x = add(mul(x, 3), 1)
#         print(x)
#         count += 1
#     return count


# print(hailstone(10))


# Showed solution to friend and stated to use infixed operators to clean code
# def hailstone(x):

#     count = 1
#     print(x)  # this is printing hailstone sequence starting at N, N =10
#     while x > 1:
#         if x % 2 == 0:  # 10 % 2 = 0
#             x = x // 2  # On first round this would result in 5, then we go into else statement
#         else:
#             x = x * 3 + 1
#         print(x)
#         count += 1
#     return count


# print(hailstone(10))
