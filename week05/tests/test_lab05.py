"""
Tests for week05 lab05.py
"""

from week05.lab05 import calculate_average_age, get_active_user_emails



def test_calculate_average_age_normal():
    users = [
        {"age": 30},
        {"age": 25},
        {"age": 35},
        {"age": "unknown"},
    ]

    assert calculate_average_age(users) == 30.0


def test_calculate_average_age_empty():
    assert calculate_average_age([]) == 0.0


def test_calculate_average_age_invalid():
    users = [
        {"age": "unknown"},
        {},
        {"age": None},
    ]

    assert calculate_average_age(users) == 0.0


def test_get_active_user_emails():
    users = [
        {"email": "alice@test.com", "is_active": True},
        {"email": "bob@test.com", "is_active": False},
        {"email": "charlie@test.com", "is_active": True},
        {"is_active": True},
    ]

    result = get_active_user_emails(users)

    assert result == ["alice@test.com", "charlie@test.com"]


def test_get_active_user_emails_empty():
    assert get_active_user_emails([]) == []


