from Final_project import *
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
    A test suite for testing our final

    NOTE:
    Typically, a test suite for a Class would be written into a second class entirely.
    However, to keep the complexity low, I chose to incorporate the test suite in a familiar way.
    In the future, we will explore how to properly write a test suite as a separate class.
    """

    # tests encrypting a normal string
    caesar = CaesarCipher()
    caesar.key = 3
    caesar.message = "A test string"

    testit(caesar.encrypt() == "D WHVW VWULQJ")


    # tests encrypting a string with punctuation
    caesar.key = 13
    caesar.message = "It's a so-so kind of day!"

    testit(caesar.encrypt() == "VG'F N FB-FB XVAQ BS QNL!")


    # tests decrypting a normal string
    caesar.key = 3
    caesar.cipher = "D WHVW VWULQJ"
    caesar.crypt_type = "decrypt"

    testit(caesar.decrypt() == "A TEST STRING")


    # tests decrypting a string with punctuation
    caesar.key = 6
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"

    testit(caesar.decrypt() == "IT'S A SO-SO KIND OF DAY!")

    # adding new tests

    # test encrypting a normal string
    caesar.key = 3
    caesar.message = "Whatever attention or affection I may shew you"

    testit(caesar.encrypt() == "ZKDWHYHU DWWHQWLRQ RU DIIHFWLRQ L PDB VKHZ BRX")

    # test encrypts a string with punctuation
    caesar.key = 14
    caesar.message = ", and Crassus,"

    testit(caesar.encrypt() == ", OBR QFOGGIG,")

    # test decrypt a string with punctuation
    caesar.key = 14
    caesar.cipher = "QWQSFC UFSSHG QOSGOF, WADSFOHCF."

    testit(caesar.decrypt() == "CICERO GREETS CAESAR, IMPERATOR.")
    # what other tests should you add?


CaesarCipher_test_suite()
