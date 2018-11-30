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

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"            # The alphabet, which will be used to do our shifts

    def __init__(self, input_file = "ciphertext.txt", key = 7, crypt_type = "decrypt"):
        """
        A constructor for the CaesarCipher class

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
        self.barcode_number = None

    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")                          # opening the input file to read it
        if self.crypt_type == "decrypt":                        # if the action is decrypt the file will be read
            self.cipher = f.read()                   # Set self.cipher to the file contents
        f.close()                                      # closing the file
        if __name__ == "__main__":
            print("File imported: {0}".format(self.input_file))

    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")                             # creating a new file to write in it the text to export
        f.write(text_to_export)
        f.close()                                           # closing the file
        if __name__ == "__main__":
            print("File exported: {0}".format(filename))

    def decrypt(self):
        """
        Converts a ciphertext.txt into an original message by shifting each letter to the left by the key

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
            print("Your message has been decrypted")
        return output

    def search_numbers(self):
        """
        This function opens the decrypted file and retrieves the integers that form the barcode to put them together into a string.
        :return:
        """
        self.barcode_number = []
        dict = {
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "ZERO": 0, "ONE": 1, "TWO": 2, "THREE": 3,
            "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7,
            "EIGHT": 8, "NINE": 9, "FIFTH": 5, "FIRST": 1,
            "SECOND": 2, "THIRD": 3, "FOURTH": 4, "SIXTH": 6,
            "SEVENTH": 7, "EIGHTH": 8, "NINTH": 9,
        }
        expo_file = open("exporting_text", "r")
        for line in expo_file:
            words = line.split()
            for word in words:
                if word in dict:
                    self.barcode_number.append(dict[word])
                else:
                    for letter in word:
                        if letter in dict:
                            self.barcode_number.append(dict[letter])

        return str(self.barcode_number).strip('[]')
