##def lsearch(arr, n, x):
##    for i in range(0, n):
##        if arr[i] == x:
##            return i  # Return index if element is found
##    return -1  # Return -1 if element is not found
##
### Input array
##arr = [1, 2, 5, 7, 31]
##x = int(input("Enter the number: "))  # Element to search
##n = len(arr)  # Length of the array
##
### Perform linear search
##result = lsearch(arr, n, x)
##
##if result == -1:
##    print("Element not found")
##else:
##    print("Element found at index:", result)


import bisect

def insert_into_sorted_list(lst, n):
    """
    Inserts an element into a sorted list while maintaining the sorted order using the bisect module.

    :param lst: List of elements (must be sorted)
    :param n: Element to insert
    :return: Updated sorted list
    """
    bisect.insort(lst, n)  # Use insort to insert into the correct position
    return lst

# Input sorted list and the element to insert
lst = [1, 2,4]
n = int(input("Enter a value to insert: "))

# Insert the element and print the updated list
print("Updated sorted list:", insert_into_sorted_list(lst, n))

             
