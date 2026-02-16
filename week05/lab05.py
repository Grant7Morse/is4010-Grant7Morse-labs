"""
Lab 05 - Refactoring a script into clean functions with error handling.

This module provides:
- calculate_average_age(users): returns average of valid integer ages
- get_active_user_emails(users): returns emails for active users with an email
"""

from typing import Any, Dict, List


# IMPORTANT:
# Replace this users list with the EXACT users list from your lab handout
# if your instructor provided one. (Keep the variable name `users`.)
users: List[Dict[str, Any]] = [
    {"name": "Alice", "age": 30, "email": "alice@example.com", "is_active": True},
    {"name": "Bob", "age": 25, "email": None, "is_active": False},
    {"name": "Charlie", "age": 35, "email": "charlie@example.com", "is_active": True},
    {"name": "Dana", "age": "unknown", "email": "dana@example.com", "is_active": True},
    {"name": "Eve", "is_active": True},  # missing keys edge case
]


def calculate_average_age(users: List[Dict[str, Any]]) -> float:
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries. A user may or may not include an "age" key.
        Some ages may be invalid (e.g., "unknown").

    Returns
    -------
    float
        Average of valid integer ages. Returns 0.0 if:
        - users is empty, or
        - no users have a valid integer age.
    """
    if not users:
        return 0.0

    total_age = 0
    count = 0

    for user in users:
        age = user.get("age")
        if isinstance(age, int):
            total_age += age
            count += 1

    if count == 0:
        return 0.0

    return total_age / count


def get_active_user_emails(users: List[Dict[str, Any]]) -> List[str]:
    """
    Get a list of emails for users who are active and have an email address.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries. Users may be missing keys like "email" or
        "is_active".

    Returns
    -------
    list of str
        Emails where BOTH conditions are true:
        - user.get("is_active") is truthy
        - user.get("email") exists and is non-empty
    """
    emails: List[str] = []

    for user in users:
        if user.get("is_active") and user.get("email"):
            emails.append(user["email"])

    return emails


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    active_emails = get_active_user_emails(users)

    print(f"Average age: {avg_age}")
    print("Active user emails:", active_emails)
