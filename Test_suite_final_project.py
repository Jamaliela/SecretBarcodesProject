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


    # tests decrypting a string with punctuation and numbers
    caesar.key = 7
    caesar.cipher = "OLSSV, V1Y UHTLZ HYL LTLS5 HUK LSH. 3L SV2L 9 OH2L H NYF 0PTL"
    testit(caesar.decrypt() == "HELLO, OUR NAMES ARE EMELY AND ELA. WE LOVE 2 HAVE A GR8 TIME")


    # adding new tests (for later)


final_project_test_suite()
