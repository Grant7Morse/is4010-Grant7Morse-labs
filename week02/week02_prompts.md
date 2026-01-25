# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> **Context:** I’m working on a Python lab. This function is supposed to return the sum of all even numbers in a list, but it’s producing the wrong result. Here is the function:
>
> ```python
> def sum_of_evens(numbers):
>     """Calculate the sum of all even numbers in a list.
>
>     Parameters
>     ----------
>     numbers : list of int
>         A list of integers.
>
>     Returns
>     -------
>     int
>         The sum of all even numbers in the list.
>     """
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
>
> **Persona:** You are a senior Python developer and code reviewer.
>
> **Task:** Identify the logical bug, explain it briefly, and provide a corrected version of the function.
>
> **Format:** Return (1) a short explanation and (2) the corrected code in a Python code block.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

    """The conditional was checking for odd numbers (num % 2 == 1) instead of evens (num % 2 == 0), so it was summing the wrong values"""

def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results

   def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user["name"] for user in users if user["age"] >= 18]

"""What I learned is that iterating directly over list elements nstead of using index-based loops makes code easier to read, and list comprehensions provide a concise, Pythonic way to filter and transform data"""


#### Problem 1: Debugging a buggy function

This function is supposed to calculate the sum of all **even** numbers in a list, but it contains a logical error.

**Your task**: Craft a prompt that asks the AI to find and fix the bug.

**Buggy code**:
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total