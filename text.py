list1 = [4, 8, 7, 9, 10, 10, 4]  

# Method 1: Using two passes (Two loops)
# Step 1: Find the maximum element
max = list1[0]  # Initialize max with the first element
for i in list1:  # Traverse the list to find the max element
    if i > max:
        max = i  

# Step 2: Find the second maximum element
sec_max = -1  # Initialize second max with -1
for i in list1:  # Traverse the list again
    if i > sec_max and i != max:  # Check for second max
        sec_max = i  

print(sec_max)  # Print the second max value

# Time Complexity: 
# - First loop: O(n) (finding max)
# - Second loop: O(n) (finding second max)
# - Total: O(n) + O(n) = O(n)
# - Space Complexity: O(1) (constant extra space)
# - Efficient and simple approach.

# -----------------------------------------------------------------

# Method 2: Sorting-based approach
list1.sort()  # Sort the list in ascending order (O(n log n))

# Traverse from the end to find the second maximum element
for i in range(len(list1)-1, 0, -1):  
    if list1[i] != list1[-1]:  # Find the first element smaller than max
        print(list1[i])
        break  # Stop once second max is found

# Time Complexity:
# - Sorting takes O(n log n)
# - Loop takes O(n) in the worst case
# - Total: O(n log n) + O(n) = O(n log n)
# - Space Complexity: O(1) (sorting is done in-place)
# - Less efficient than Method 1 due to sorting overhead.

# -----------------------------------------------------------------

# Method 3: Single-pass approach (Efficient)
max1 = list1[0]  # Initialize max
sec1 = -1  # Initialize second max

for i in range(len(list1)):  # Traverse the list in one pass
    if list1[i] > max1:  # If a new max is found
        sec1 = max1  # Update second max before changing max
        max1 = list1[i]  
    elif list1[i] > sec1 and list1[i] < max1:  
        sec1 = list1[i]  # Update second max only if it's smaller than max

print(sec1)  # Print the second max value

# Time Complexity:
# - Only a single pass through the list: O(n)
# - Space Complexity: O(1) (no extra space used)
# - Most efficient approach as it finds second max in a single pass.
