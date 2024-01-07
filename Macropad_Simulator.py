"""
Written by Owen McCall
Boston University Metropolitan College
"""


class Macropad:
    """ Representation of the macropad and the script running there"""

    def __init__(self):
        self.lights = ["Off" for i in range(12)]
        self.__erase_mode = False
        self.keys = dict(enumerate('ABCDEFGHIJKL'))
        self.colors = {"Red", "Blue"}

    """Sets up lights corresponding to each key on the macropad, on status is
    having it's color be included in the instantiated set, erase mode is kept
    track of with a boolean as it a toggled state, keys is identical to dict
    used in real macropad for output.
    These init lines are have nearly identical meaning to the first few lines of
    the macropad code. """

    def __toggle_erase_mode(self):
        self.__erase_mode = not self.__erase_mode
        for i in range(12):
            # if in erase mode set all lit lights to red
            if self.__erase_mode and self.lights[i] in self.colors:
                self.lights[i] = "Red"
            if not self.__erase_mode and self.lights[i] in self.colors:
                self.lights[i] = "Blue"

    """ Private method for the programmed effect of pressing the encoder dial 
    down instead of pressing a key, toggles erase mode and lights based on mode.
    """

    def get_erase_mode(self):
        return self.__erase_mode

    """ This method gives the erase ode the ability to affect the output of key 
    presses like it does in the macropad's script. """

    def key_press(self):
        user_input = -2
        while True:
            try:
                user_input = int(input("Please enter a number 1-13 for"
                                       " key/dial entry, or 0 to exit:"))
                assert 0 <= user_input <= 13
            except:
                print("Incorrect entry, please try again.")
                continue
            else:
                break
        if user_input == 13:
            self.__toggle_erase_mode()
            print("Erase Mode toggled, this print statement represents the "
                  "lights color changing")
            return "erase"
        if user_input != 0:
            if self.__erase_mode:
                self.lights[(user_input - 1)] = "Off"
                return tuple(['E', self.keys[user_input - 1]])
            else:
                if self.lights[user_input - 1] == "Off":
                    self.lights[user_input - 1] = "Blue"
                    return tuple(['C', self.keys[user_input - 1]])
                else:
                    return tuple(['P', self.keys[user_input - 1]])
        else:
            return 0

    """ This method represents the users entry of information into the macropad 
    through key or dial presses and the output via serial connection, this a
    closer representation of the content of the while true loop from the 
    macropad script.
    Additionally, an option for an exit from the testing program is made 
    available via -1 which is not from the original, but is used for testing in 
    the main scripts loop. """

    def __len__(self):
        output = 0
        for i in self.lights:
            if i != 0:
                output += 1
        return output

    """ Magic method for checking the number of occupied keys"""

    def __str__(self):
        return "Lights: " + str(self.lights) + "\n" + "Erase mode: " + \
            str(self.__erase_mode) + "\n"

    """ String representation of current state of Macropad. """

    def for_testing(self):
        self.__toggle_erase_mode()

    """ used purely for testing"""


# Testing area
if __name__ == "__main__":
    macropad = Macropad()

    assert macropad.get_erase_mode() == False
    """get_erase_mode() test"""

    assert len(macropad) == 0
    """__len__() test"""

    macropad.for_testing()
    assert macropad.get_erase_mode() == True
    """__toggle_erase_mode() test"""
