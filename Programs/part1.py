# Part 1:
# Given the following list, write a program that will determine which of the integers
# in the list are not repeated (are unique).  Print out the unique integers from the
# list.

integers = [9,2,4,3,2,6,7,7,9]
def unique_integers(integers):
    unique_list = []
    for i in integers:
        if i not in unique_list:
            unique_list.append(i)
    for i in unique_list:
        print(i)
unique_integers(integers)

