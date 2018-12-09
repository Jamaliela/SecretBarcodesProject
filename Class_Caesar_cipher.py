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


class CeasarCipher:
    """
    The CaesarCipher class represents and manipulates key, input file and the crypt type
    This class will import a file that needs to be encrypted or decrypted, with an integer representing the key
    it will decrypt or decrypt the given file
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"            # The alphabet and numbers, which will be used to do our shifts

    def __init__(self, input_file = "message_to_receive.txt", key = 7, crypt_type = "decrypt"):
        """
        A constructor for the CaesarCipher class that decrypts secret code
        :param input_file: The file to be decrypted
        :param key: The amount each message/cipher needs shifted
        :param crypt_type: Either encrypt or decrypt
        """
        self.input_file = input_file                            # The file to be encrypted or decrypted
        self.key = key                                          # The amount each message/cipher will be shifted
        self.message = ""                                       # A placeholder for the message
        self.cipher = ""                                        # A placeholder for the cipher
        self.crypt_type = crypt_type                            # Either "encrypt" or "decrypt"
        self.import_file()                                      # Calls the import_file() method below
        self.barcode_number = None                              # initializing the barcode number

    def import_file(self):
        """
        Imports a file stored in the variable self.input_file in order to use it for decryption
        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")                          # opening the input file to read it
        if self.crypt_type == "decrypt":                        # if the action is decrypt the file will be read
            self.cipher = f.read()                   # Set self.cipher to the file contents
        elif self.crypt_type == "encrypt":           # encrypting the message in another py file
            self.message = f.read()                     # reading message
        f.close()                                      # closing the file
        if __name__ == "__main__":                      # conditional lines to inform user that hte file has been imported
            print("File imported: {0}".format(self.input_file))

    def export_file(self, text_to_export, filename):
        """
        creates a file if it doesn't exist and writes in it to export it

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")                             # creating a new file to write in it the text to export
        f.write(text_to_export)                             # opening the file
        f.close()                                           # closing the file
        if __name__ == "__main__":
            print("File exported: {0}".format(filename))    # prints text to inform user that file is ready

    def encrypt(self):
        """
        Converts an original message into a ciphered message with each letter shifted to the right by the key
        :return: a string representing the messagetext.txt
        """
        output = ""                             # starting up an empty string
        for i in self.message:                                  # for loop to access the message
            if i.upper() in self.alphabet:                          # for every letter in the alphabet
                old_letter = self.alphabet.find(i.upper())
                # Uses modulus to return the correct index for each letter after the shift
                # (for cases where the index is outside the range of self.alphabet,
                #  it wraps back to the beginning of the alphabet)
                output += self.alphabet[(old_letter + self.key) % 36]     # provides the output after the shifting
            else:
                output += i         # Adds non-alphabet characters directly
        if __name__ == "__main__":
            print("Message Encrypted")
        return output

    def decrypt(self):
        """
        Converts a message_to_receive.txt into an original message by shifting each letter to the left by the key
        :return: a string representing the original message
        """
        # TODO Complete the decrypt method
        output = ""
        for i in self.cipher:                                   # for loop to shift letters for decryption
            if i.upper() in self.alphabet:                      # if letters are upper case
                new_letter = self.alphabet.find(i.upper())
                # we use the module to return the correct module after the inverse
                # when the index is negative it will go back to the end of the alphabet
                output += self.alphabet[new_letter - self.key % 36]
            else:
                output += i     # Adds non-alphabet characters directly
        if __name__ == "__main__":
            print("Your message has been decrypted")                # informing user that the file has been decrypted.
        return output

    def search_numbers(self):
        """
        This function opens the decrypted file and retrieves the integers that form the barcode to put them together into a string.
        :return: a barcode in string form
        """
        self.barcode_number = []                                # starting a list to add the barcode numbers
        dict_to_use = {                                                # creating a dictionary and its values and keys
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3,
            "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7,
            "EIGHT": 8, "NINE": 9, "FIFTH": 5, "FIRST": 1,
            "SECOND": 2, "THIRD": 3, "FOURTH": 4, "SIXTH": 6,
            "SEVENTH": 7, "EIGHTH": 8, "NINTH": 9,
        }
        expo_file = open("exporting_text", "r")                     # opening the decrypted file as new name and reading it
        for line in expo_file:                                      # accessing each line in the file
            words = line.split()                                    # splitting the words in the lines
            for word in words:                                      # accessing every word in the file
                if word in dict_to_use:                                    # if the word is in the dictionary
                    self.barcode_number.append(dict_to_use[word])          # each word that is a number will be retrieved and appended to barcode
                else:                                               # otherwise
                    for letter in word:                             # each letter will be checked and the numbers will be retrieved
                        if letter in dict_to_use:
                            self.barcode_number.append(dict_to_use[letter])      # the retrieved numbers are appended in the barcode
        string_barcode_number = ""                                  # converting the barcode to a string
        for i in self.barcode_number:                               # for every element in the barcode
            string_barcode_number += str(i)                         # the element will be added to as string
        return string_barcode_number
