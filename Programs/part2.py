# Given the following list of integers, write a program that will determine if the list
# is a palendrome.  That is, if the list were reversed, it would read the same as the
# unreversed list.

integers = [1,2,3,4,5,4,3,2,1]  # note, this is a palendrome, so your program
# should report 'true'
# integers = [2,3,5,7,1,24,8]#error handling test, should print false
reverse = integers[::-1]#swap the list around
  
res = integers == reverse 
print("Is list Palindrome : " + str(res))