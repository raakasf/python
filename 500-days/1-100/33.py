import bisect

sorted_list = [1, 2, 4, 5]
# The bisect module is used for maintaining a list in sorted order without having to sort it after each insertion.
# It provides functions like bisect() and insort() which help in inserting elements into a sorted list at the correct position.
# Internally, it uses binary search to find the correct index where 3 should go.
bisect.insort(sorted_list, 3)
print(sorted_list)
