def sum_up_to(n):
    if n == 1:
        return 1
    return n + sum_up_to(n - 1)


def multiply_list(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] * multiply_list(lst[1:])


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(sum_up_to(5))
print(multiply_list([2, 3, 5, 7, 8]))
print(is_palindrome("rotator"))
print(is_palindrome("rotovator"))
