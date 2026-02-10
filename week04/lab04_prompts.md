# Lab 04 – AI Data Structure Recommendations

## Problem 1: Finding common items
**Prompt used:**
What Python data structure should I use to efficiently find common elements between two very large lists? Order does not matter.

**AI Recommendation & Reasoning:**
The AI recommended using a **set** because sets support fast membership testing and intersection operations. Converting lists to sets and finding their intersection is more efficient than nested loops.

---

## Problem 2: User profile lookup
**Prompt used:**
I have a list of user dictionaries with unique usernames. I need to frequently look up a user by name and performance is critical. What data structure should I use?

**AI Recommendation & Reasoning:**
The AI recommended using a **dictionary**, mapping usernames to user objects, because dictionaries provide O(1) average lookup time.

---

## Problem 3: Listing even numbers in order
**Prompt used:**
I need to filter even numbers from a list while preserving the original order. What Python data structure or approach should I use?

**AI Recommendation & Reasoning:**
The AI recommended using a **list** with a loop or list comprehension, because lists preserve order and are ideal for sequential filtering.
