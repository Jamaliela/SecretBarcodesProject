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

encryption = cipher.CeasarCipher("messagetext.txt", 7, "encrypt")
exporting = encryption.encrypt()                                 # decrypting the file
encryption.export_file(exporting, "message_to_receive")              # naming the new file that has been decrypted
