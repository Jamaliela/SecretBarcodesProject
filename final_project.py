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
import Class_barcode as barcode
#

def main():

    wn = self.tess.Turtle
    text1 = cipher.CeasarCipher("ciphertext.txt", 7, "decrypt")        # assigning text1 the class and opening the message to decrypt
    exporting = text1.decrypt()                                 # decrypting the file
    text1.export_file(exporting, "exporting_text")              # naming the new file that has been decrypted
    print(text1.search_numbers())
    upc_barcode = barcode.Barcode()
    upc_barcode.is_valid_input()
    # upc_barcode.is_valid_modulo()
    # upc_barcode.translate()

main()
