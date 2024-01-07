"""
Written by Owen McCall
Boston University Metropolitan College
"""
import copy as Copy

class Desktop:
    """Representation od my desktop computer and the script that runs on it in
    tandem with the connected macropad."""

    def __init__(self, clipboard_contents):
        self.__clipboard = clipboard_contents
        self.content = {chr(i): "" for i in range(65, 77)}
        self.empty_slots = 12
    """Init method that accounts for script starting with an occupied clipboard.
    Also inits the extra clipboard slots with the corresponding letter that
    will be sent from the macropad.
     Empty slots is not from the real script, but is used here for testing."""

    def get_clipboard(self):
        return self.__clipboard
    """Getter for clipboard, represents ctrl+v from either manual entry or 
    script entry. This also represents the copying of data fro the clipboard 
    using the pyperclip module. """

    def set_clipboard(self, string):
        self.__clipboard = string
    """Setter for clipboard, represents ctrl+c from either manual or scrip 
    entry."""

    def copy_event(self, key):
        # save clipboard
        temp = Copy.copy(self.get_clipboard())

        # this line represents a scripted ctrl+v entry
        self.set_clipboard(input("Please enter text to be copied:"))

        # store new entry
        self.content[key] = Copy.copy(self.get_clipboard())

        # decrement empty slots
        self.empty_slots -= 1

        # check for ctrl+c call w/o highlighted text, if so set to empty as
        # the above ctrl+c call won't overwrite with empty string
        if temp == self.content[key]:
            self.content[key] = ""

        # set clipboard back to original entry
        self.set_clipboard(temp)

        # return report of event
        return tuple(["Copy", str(key), self.content[key]])
    """Close representation of the copy function in the Desktop script with
    report for testing"""

    def paste_event(self, key):
        # save clipboard
        temp = Copy.copy(self.get_clipboard())

        # set content to clipboard for pasting
        self.set_clipboard(Copy.copy(self.content[key]))

        # this print will simulate the paste triggered by the desktop script
        print(self.get_clipboard())

        # set clipboard back to original entry
        self.set_clipboard(temp)

        # return report of event
        return tuple(["Paste", str(key), self.content[key]])
    """Close representation of the paste function on the desktop script, prints 
    to terminal to signify a successful paste, returns report for testing"""

    def erase_event(self, key):
        self.content[key] = ""
        # increment empty slots
        self.empty_slots += 1
        return tuple(["Erase", str(key)])
    """ Identical function to what is used on desktop """

    def read_connection(self, input_bytes):
        action = ord(input_bytes[0])
        keynum = input_bytes[1]
        if action == 67:
            self.copy_event(keynum)
        if action == 69:
            self.erase_event(keynum)
        if action == 80:
            self.paste_event(keynum)
    """ This method is nearly identical to the content of the main while loop 
    from the desktop script. """
    def __str__(self):
        output = "Clipboard entry: " + self.get_clipboard() + "\n"
        for i in self.content.items():
            output = output + ("Extra Clipboard entry " + str(i[0]) + ": " + i[1] +
                               "\n")
        return output
    """String representation of the Desktop scripts data"""


# Testing area
if __name__ == "__main__":
    desktop = Desktop("test")

    assert desktop.get_clipboard() == "test"
    """get_clipboard() test"""

    desktop.set_clipboard("new")
    assert desktop.get_clipboard() == "new"
    """set_clipboard test"""

    assert desktop.copy_event('A') == ("Copy", 'A', desktop.content['A'])
    """copy_event() test"""

    assert desktop.paste_event('A') == ("Paste", "A", desktop.content['A'])
    """paste_event() test"""

    assert desktop.erase_event('A') == ("Erase", 'A')
    """erase_event() test"""

    desktop.content['A'] = 0
    desktop.read_connection(('C', 'A'))
    assert desktop.paste_event('A') == ("Paste", "A", desktop.content['A'])
    """read_connection() test"""

    print("All tests passed successfully")
























