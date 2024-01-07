"""
Written by Owen McCall
Boston University Metropolitan college
"""

from Macropad_Simulator import Macropad
from Desktop_Simulator import Desktop


if __name__ == "__main__":

    macropad = Macropad()
    desktop = Desktop("initial clipboard")
    """ Init the two simulators, this represents the macropad starting up, the
    desktop script being run, and their ability to connect to eachother (by
    the fact the being in the same script makes that able to interact like in
    the following while loop)."""

    while True:
        user_input = macropad.key_press()
        if user_input == "erase":
            continue
        if user_input == 0:
            break
        desktop.read_connection(user_input)
    """ This combines the two while true loops of the macropad and desktop 
    scripts, since the desktop reads the connectio at a rate of 10 times per 
    second I feel it's acceptable to represent the connection with an immediate
    response."""

    while True:
        try:
            user_input = input(
                "Would you like a printout of the status and contents"
                "of the macropad and desktop scripts? (yes/no): ")
            assert user_input in ['yes', 'no']
        except AssertionError:
            print("Incorrent entry.")
            continue
        else:
            if user_input == "yes":
                with open("output.txt", "w") as file:
                    file.write(str(macropad))
                    file.write(str(desktop))
                    break
            else:
                print("Simulation complete.")
                break
    """ This loops is for promptinf for output."""
