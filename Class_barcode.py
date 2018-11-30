######################################################################
# Author: Ela Jamali & Emely Alfaro Zavala
# Username: Jamalie & Alfarozavalae
#
# Assignment: Final Project
#
# Purpose: Our program will receive a ciphered message with different characters and will extract the the 12-digit
# codes found and check for a barcode, afterwards, using the urllib our program will access the web showing the item
# online.
####################################################################################
# Acknowledgements:

##################################################################################
import Class_Caesar_cipher as cipher

class Barcode:
    """

    """

    def __init__(self):
        """

        :param upc_barcode:
        """
        barcode_test = cipher.CeasarCipher("ciphertext.txt", 7, "decrypt")
        self.upc_barcode = barcode_test.search_numbers()
        self.turtle = None

    def is_valid_input(self):
        """
    This function verifies if the barcode is 12 digits and if they are all positive numbers.
    :param upc_barcode:  parameter that takes the user's input to check if it is a valid 12 digit or not
    :return: Fruitful. a True or False Boolean value.
    """

        if len(self.upc_barcode) == 12 and self.upc_barcode.isnumeric():     # checks the user's input to see if it is a valid 12 digit barcode
            return True                                                      # true when the barcode is 12 digits
        return False                # returns false when it is not 12 digits input
