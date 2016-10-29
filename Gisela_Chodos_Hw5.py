"""
Prompt user for a correct PIN no more than three times.
Usage:
    python3 Gisela_Chodos_Hw5.py
"""
#!/usr/bin/env python
import sys

def getInput():
    """
    Prompt user for PIN and read keyboard input.
    Prints error message if:
        PIN contains non-numeric character(s),
        PIN does not contain exactly four digits,
        PIN is not 1234.
    Args:
        None
    Returns:
        True, if the PIN is correct.
    """
    print("\nEnter your PIN:")
    userPIN = input()       # read keyboard input
    if userPIN.isdigit():   # no non-numeric characters
        if len(userPIN) == 4: 
            if userPIN == "1234": 
                print("Your PIN is correct.\n")
                return userPIN
            else:           # PIN is not 1234
                print("Your PIN is incorrect.")
        else:               # PIN is not 4 digits long
            print("Invalid PIN length.  Correct format is: <9876>.")
    else:                   # PIN has non-numeric character
        print("Invalid PIN character.  Correct format is: <9876>.")


# Main function
def main():
    """
    Prompt user for PIN no more than 3 times.
    Print "Your bank card is blocked" after three incorrect PIN attempts.
    Args:
        None
    """
    for i in range(0,3):# loop three times
        if getInput():  # evaluates as True if a PIN has been returned from getInput()
            return      # end program if correct PIN is entered
        if i == 2:      # third try
            print("\nYour bank card is blocked.\n")
            exit(1)
    


if __name__ == '__main__':
    # Call Main
    main()
    exit(0)


