"""All about IO."""
from __future__ import division
from __future__ import print_function
import json


def success_is_relative():
    """Read from a file.

    Read the success message from week 1, but from here, using a relative path.
    TIP: remember that it's relative to your excecution context, not this file.
         The tests are run from the code1161base directory, that's the
         excecution context for this test.
    TIP: check that there ins't unwanted whitespace or line endings in the
         response. Look into .strip() and see what it does.
    """
    mode = "r"
    file_path = "../week1/pySuccessMessage.json"
    success_file = open(file_path, mode)
    response = success_file.read()
    print (response)
    success_file.close()
