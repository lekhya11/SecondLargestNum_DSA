# SecondLargestNum_DSA
Finding the Second Maximum Element in a List

# Overview

This repository contains three different methods to find the second largest number in a given list of integers.

Methods Used

# Method 1: Two-Pass Approach

First, iterate through the list to find the maximum element.

Then, iterate again to find the largest element that is not the maximum.

# Time Complexity: O(n) (Two passes of O(n) each)

# Space Complexity: O(1)

 # Method 2: Sorting-Based Approach

Sort the list in ascending order.

Iterate from the end to find the first element smaller than the maximum.

# Time Complexity: O(n log n) (Due to sorting)

# Space Complexity: O(1)


# Method 3: Single-Pass Approach (Most Efficient)

Traverse the list once while maintaining the maximum and second maximum.

# Time Complexity: O(n) (Single pass)

# Space Complexity: O(1)


# Best Approach

Method 3 is the most efficient as it finds the second maximum in a single pass O(n) without sorting or using extra space.

# How to Run the Code

Copy and paste the code into a Python script (second_max.py).

# Run the script using:

python second_max.py

The output will display the second largest number found using the three methods.
