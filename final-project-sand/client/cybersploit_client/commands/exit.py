from ..commands import Command # Required
from .. import actions # Example to import the actions folder
# from ..util import config # Example to import a utility


class ExitCommand(Command): # Call the class anything you'd like
    """
    Exit the CLI.
    """
    # The text above, known as the docstring, is also shown when using the help command in the terminal

    # When 
    def do_command(self, lines: str):
        # just for demo purposes. Note that the input is a single string, and if no arguments are passed, just gives an empty string
        # If you want to force arguments passed in, you will have to add a check for that.
        print(f"Found input: {lines}")
        print("Exiting CLI")
        # Return true is how we fully exit. In basically all other commands, don't return anything/return None
        return True 

command = ExitCommand # Assign the class you created to the variable called command for the system to find the command!
