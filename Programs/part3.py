# Write a program that takes in a suggested password from a user.  The program should
# require the password string to contain:

# 	At least one lowercase letter [a-z]
# 	At least one digit [0-9]
# 	At least one uppercase letter [A-Z]
# 	At least one symbol from [$#@]
# The password string must be anywhere from 6 to 12 characters, inclusive.
# The program should take in the string, perform the determination, and print out
# either 'accepted' or 'rejected', and if rejected state why (which rule was violated).

password = input("Please enter a password: ")
def password_check(password):
      
    SpecialSym =['$', '@', '#']#special symbol
    val = True
      
    if len(password) < 6:#no less than 6
        print('length should be at least 6')
        val = False
        # if val == False:
        #     print("Rejected!")
          
    if len(password) > 12:#no more than 12
        print('length should be not be greater than 12')
        val = False
        if val == False:
            print("Rejected!")
          
    if not any(char.isdigit() for char in password):#at least one digit
        print('Password should have at least one numeral')
        val = False
        # if val == False:
        #     print("Rejected!")
          
    if not any(char.isupper() for char in password):#at least one uppercase
        print('Password should have at least one uppercase letter')
        val = False
        # if val == False:
        #     print("Rejected!")
          
    if not any(char.islower() for char in password): #at least one lowercase
        print('Password should have at least one lowercase letter')
        val = False
        # if val == False:
        #     print("Rejected!")
          
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
        # if val == False:
        #     print("Rejected!")

def main():
    if password_check(password):#is the password val true or false, if true:
        print("Accepted!")
    else:#if false
        print("Rejected!")
#dunder
if __name__ == '__main__': #explanation here https://www.freecodecamp.org/news/if-name-main-python-example/
    '''So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
    But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.'''
    main()
# g6@Hjkl #good password here
