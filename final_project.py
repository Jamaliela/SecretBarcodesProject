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
import Class_Caesar_cipher as cipher                 # importing the ceasar_cipher class with the name cipher
import Class_barcode as barcode                            # importing the barcode class with the name barcode
import turtle                                           # importing the turtle library
import webbrowser                                       # importing the webbrowser library


def main():
    global barcode_digits                               # making the barcode digits a global variable
    wn = turtle.Screen()                                # creating the turtle screen

    text1 = cipher.CeasarCipher("C:\\Users\\Jamalie\\Google Drive\\CSC226P01\\message_to_receive.txt", 7, "decrypt")        # assigning text1 the class and opening the message to decrypt
    exporting = text1.decrypt()                                 # decrypting the file
    text1.export_file(exporting, "exporting_text")              # naming the new file that has been decrypted
    barcode_digits = text1.search_numbers()                     # calling the search function to retrieve the barcode
    upc_barcode = barcode.Barcode()                             # calling the barcode class with the upc_barcode name
    upc_barcode.is_valid_input()                                # calling the is_valid function to check if the numbers are a valid 12 combination
    upc_barcode.is_valid_modulo()                               # calling the is_valid_modulo to check if it is an actual barcode
    upc_barcode.translate()                                     # calling the translate function so translate the barcode to the binary lists
    upc_barcode.position()                                      # calling the function that draws the barcode
    wn.onclick(open_browser)                                    # this line enables the user to click on the screen and runs the open_browser function
    wn.mainloop()                                               # window screen as loop


def open_browser(x, y):
    """
    This function is for taking the barcode digits and going to the look up website to show the item
    :param read: variable to put together the barcodelookup website and the digits.
    :return: Void.
    """
    global barcode_digits                   # using the barcode_digits variable as global
    read = webbrowser.open('https://www.barcodelookup.com/' + barcode_digits)       # opening the website that results from adding the digits to the barcode look up webpage


main()
