from final_project import *
import sys


def testit(did_pass):
    """  Prints the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def final_project_test_suite():
    """
    A test suite for testing the decrypt methods of the class

    NOTE:
    Typically, a test suite for a Class would be written into a second class entirely.
    However, to keep the complexity low, I chose to incorporate the test suite in a familiar way.
    In the future, we will explore how to properly write a test suite as a separate class.
    """

    # tests decrypting a normal string
    caesar = CeasarCipher()
    caesar.key = 7
    caesar.cipher = "0OPZ TLZZHNL OHZ 0V IL"
    caesar.crypt_type = "decrypt"

    testit(caesar.decrypt() == "THIS MESSAGE HAS TO BE")


    # tests decrypting a string with punctuation
    caesar.key = 6
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"

    testit(caesar.decrypt() == "IT'S A SO-SO KIND OF DAY!")

    # adding new tests

    testit(caesar.decrypt() == "CICERO GREETS CAESAR, IMPERATOR.")
    # what other tests should you add?


final_project_test_suite()
