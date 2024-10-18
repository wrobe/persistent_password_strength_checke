""" Script: persistent_password_strength_checker.py
    Description: Type your poassword to see if is cracable.
    Author: Krzysztof Wróbel
    Modified: Sept 2023
    Note: This script will not display or store user input. 
    This script is only to check
    if your password is strong. 
"""
import getpass


def check_strength(passwd: str) -> bool:
    """A strong password must be at least 10 characters long
       and must contain a lower case letter, an upper case letter,
       and at least 3 digits.
       Returns True if passwd meets these criteria, otherwise returns False.
    """
    # check password length
    if len(passwd) < 10:
        return False

    # check password for uppercase, lowercase and numeric chars
    hasupper = False
    haslower = False
    digitcount = 0
    for char in passwd:
        if char.isupper():
            hasupper = True
        elif char.islower():
            haslower = True
        elif char.isdigit():
            digitcount += 1
    
    # check if all conditions are satisfied
    outcome = bool(hasupper and haslower and digitcount >= 3)
    return outcome


def main():
    """main function, ask user input, then check its strength"""

    while True: 
        passwd = getpass.getpass("Enter your password to check its strength: ")
        result = check_strength(passwd)
        if result:
            print(f"[*] Password is strong\n")
            break
        else:
            print(f"[*] Password is NOT strong. Please try again.\n")


    # unit tests - KEEP THIS CODE UNCHANGED
    print("====\nUnit tests\n====")
    try:
        tests = {"aX238": False,
                 "Password123": True,
                 "Password": False,
                 "my_password1234": False,
                 "p3tral0vesP1thon": True}
        for test, result in tests.items():
            assert check_strength(test) == result, \
                      print(f"{test} should return {result}, check your code")
            print(f"{test} correctly returns {result}")
    except AssertionError:
        print("Remaining tests not carried out because the above failed")


if __name__ == "__main__":
    main()