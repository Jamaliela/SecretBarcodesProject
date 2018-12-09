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
import Class_Caesar_cipher as cipher                # importing the ceasar_cipher class with the name cipher
import turtle                                       # importing the turtle library


class Barcode:
    """
    Takes a 12 digit number and check for barcode, if it's a valid one, it draws it and the turtle screen can be click to access barcode online.
    """

    def __init__(self):
        """
        A constructor for the barcode class that will check for barcodes and draws them with turtles.
        """
        barcode = cipher.CeasarCipher("exporting_text", 7, "decrypt")            # taking the barcode from the Caesar cipher class
        self.upc_barcode = barcode.search_numbers()                              # calling the return value from the search number function in the caesar cipher class.
        self.tess = turtle.Turtle()                                     # creating tess, a turtle object
        self.left1 = ""                                                 # starting the left side for the barcode drawing
        self.rights = ""                                               # starting the right side for the barcode drawing
        self.guard_left = ""                                               # starting the left guard side for the barcode drawing
        self.center_left = ""                                               # starting the left center side for the barcode drawing
        self.guard_center = ""                                              # starting the center guard for the barcode drawing
        self.center_right = ""                                              # starting the right center side for the barcode drawing
        self.guard_right = ""                                                 # starting the right guard for the barcode drawing

    def is_valid_input(self):
        """
        This function verifies if the barcode is 12 digits and if they are all positive numbers.
        :return: Fruitful. a True or False Boolean value.
        """

        if len(self.upc_barcode) == 12: # checks the user's input to see if it is a valid 12 digit barcode
            return True                                       # true when the barcode is 12 digits
        else:
            self.upc_barcode = input("Invalid barcode number. No barcode found")    # program will inform that no barcode has been found

    def is_valid_modulo(self):
        """
        This function will check if the 12 digit numbers form a valid barcode by using the module check character.
        :param self: takes the user's input and does several operations to the odd and even positions with the module check character method.
        :return: checkdigit (the variable that should match the last digit of the barcode
        """
        oddnumbers = []                             # creating new list
        for i in range(0,len(self.upc_barcode),2):           # creating for loop to go through the elements in the barcode starting from the first one (odd) and skipping every other one
            oddnumbers.append(self.upc_barcode[i])           # appending into the oddnumbers list each of the elements retrieved in the for loop
        oddnumber_sum = sum(map(int,oddnumbers))    # adding all the elements in the list created and using map to make them integers
        oddbythree = int(oddnumber_sum) * 3         # multiplying the oddnumber_sum by three as one of the steps in module check character

        evennumbers = []                            # creates new empty list for even numbers
        for i in range(1,len(self.upc_barcode),2):           # for loop to start in the first even element of the barcode and skipping every other one
            evennumbers.append(self.upc_barcode[i])          # appending the retrieved even numbers into the empty list
        evennumbers = evennumbers[:-1]              # taking out the last even number (module check character)
        evennumber_sum = sum(map(int, evennumbers))  # adding all the even numbers after changing them into integers.
        final = oddbythree + evennumber_sum         # adding the result from odd numbers and even numbers to get to the final step
        final = final % 10                          # checking if the final number is divisible by 10 with modulus
        if final is not 0:                          # if function to check if the final digit is not zero
            checkdigit = 10 - final                 # subtracting 10 from the final one when the final is not zero
        else:
            checkdigit = final     # if there's no remainder in modulus of final % 10 the final value stays the same
        return checkdigit                           # returning the checkdigit value

    def translate(self):
        """
        This function will translate the barcode into binary numbers so that we can draw the turtle by using the turtle module
        :return: Fruitful. returns leftl and rights values of the lists lefside and rightside
        """
        leftside = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']  # creating a list with all the elements from the left side table.
        rightside = ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']          # # creating a list with all the elements from the right side table.
        self.upc_barcode = list(self.upc_barcode)                     # making the barcode a list
        self.left1 = []                                  # creating empty list to go through the first 6 elements of barcode
        for i in self.upc_barcode[0:6]:                      # for loop to run in the first 6 elements
            lf = leftside[int(i)]                   # getting the first six elements of the list
            self.left1.append(lf)                        # appending the first 6 elements into the leftl variable
        self.rights = []                                 # creating an empty list to go through the remainder 6 elements of barcode
        for i in self.upc_barcode[6:12]:                     # for loop to run in the remainder 6 elements
            rs = rightside[int(i)]                  # getting the first six elements of the list
            self.rights.append(rs)                       # appending the first 6 elements into the leftl variable
        return self.left1, self.rights                        # returning both leftl and rights to use them in main for drawing

    def drawing_blackline(self):
        """
        This function will create black lines according to the binary values for the barcode
        :return: None. Void
        """

        self.tess.color("black")                            # setting the color of the turtle to be black
        self.tess.begin_fill()                              # beginning to fill with the turtle
        for i in range(2):                          # for loop to run twice
            self.tess.forward(2)                            # turtle t moves forward by 2
            self.tess.left(90)                              # turtle t turns 90 degrees left to go up
            self.tess.forward(200)                          # turtle t goes forward 200 up
            self.tess.left(90)                              # turtle t turns 90 degrees left again
        self.tess.end_fill()                                # finishing the filling of t
        self.tess.forward(2)                                # moving to the right by 2 without leaving a trace

    def drawing_blackline_long(self):
        """
        This function will create long black lines according to the binary values for the barcode
        :return: None. Void
        """
        self.tess.color("black")                            # setting the color of the turtle to be black
        self.tess.begin_fill()

        for i in range(2):                          # for loop to run twice
            self.tess.forward(2)                            # turtle t moves forward by 2
            self.tess.left(90)                              # turtle t turns 90 degrees left to go up
            self.tess.forward(248)                          # turtle t goes forward 248 up
            self.tess.left(90)                              # turtle t turns 90 degrees left again
        self.tess.end_fill()                                # finishing the filling of t
        self.tess.forward(2)                                # moving to the right by 2 without leaving a trace

    def drawing_white_line(self):
        """
        This function will create black lines according to the binary values for the barcode
        :return: none. Void function .
        """
        self.tess.color("white")                            # setting the color of the turtle to be black
        self.tess.begin_fill()                              # beginning to fill with the turtle
        for i in range(2):                          # for loop to run twice
            self.tess.forward(2)                            # turtle t moves forward by 2
            self.tess.left(90)                              # turtle t turns 90 degrees left to go up
            self.tess.forward(200)                          # turtle t goes forward 200 up
            self.tess.left(90)                              # turtle t turns 90 degrees left again
        self.tess.end_fill()                                # finishing the filling of t
        self.tess.forward(2)                                # moving to the right by 2 without leaving a trace

    def drawing_white_line_long(self):
        """
        This function will create long white lines according to the binary values for the barcode
        :return: none. Void function .
        """
        self.tess.color("white")                            # setting the color of the turtle to be black
        self.tess.begin_fill()
        for i in range(2):                          # for loop to run twice
            self.tess.forward(2)                                # moving to the right by 2
            self.tess.left(90)                              # turtle t turns 90 degrees left to go up
            self.tess.forward(248)                          # turtle t goes forward 248 up
            self.tess.left(90)
        self.tess.end_fill()                                # finishing the filling of t
        self.tess.forward(2)                                # moving to the right by 2 without leaving a trace

    def position(self):
        """
        This class controls the position so that the barcode can be drawn taking the black and white lines functions in the class.
        :return: the barcode string that is shown in the turtle screen
        """
        self.tess.hideturtle()                              # hiding turtle to move its position
        self.tess.speed(0)                                  # setting the speed of the turtle
        self.tess.penup()                                   # putting the pen up to start moving
        self.tess.setpos(-250, -100)                        # setting the left side position
        left, right = self.translate()        # calling the two return variables from the translate function

        self.guard_left = ["1", "0", "1"]                # creating list for left guard
        for i in self.guard_left:                        # loop for left guard
            if i == "0":                            # if function for drawing white lines when i is 0
                self.drawing_white_line_long()
            else:
                self.drawing_blackline_long()               # # if function for drawing white lines when i is 0

        self.tess.setpos(-244, -52)                         # setting the position

        for i in range(len(left)):                  # for loop to run in the len of the first 6 elements retrieved for the left side
            for j in left[i]:                       # nested for loop to run in the first 6-digit binary element inside the left side list
                if j == "0":                        # if the element is zero then
                    self.drawing_white_line()           # a white line is drawn
                else:
                    self.drawing_blackline()            # if it is anything else a black line is drawn

        self.tess.setpos(-160, -100)

        guard_center = ["0", "1", "0", "1", "0"]        # creating list for center guard
        for i in guard_center:                          # loop for center guard
            if i == "0":                                 # if function for drawing white lines when i is 0
                self.drawing_white_line_long()
            else:
                self.drawing_blackline_long()           # drawing black lines when i is not 0

        self.tess.setpos(-150, -52)                         # setting the position
        for i in range(len(right)):                 # for loop # for loop to run in the len of the first 6 elements retrieved for the center side
            for j in right[i]:                      # nested for loop to run in the first 6-digit binary element inside the center side list
                if j == "0":                        # if the element is zero then
                    self.drawing_white_line()           # a white line is drawn
                else:
                    self.drawing_blackline()            # if it is anything else a black line is drawn
        self.tess.setpos(-66, -100)                         # setting the position

        # right guard
        guard_left = ["1", "0", "1"]                # creating the list for the left guard
        for i in guard_left:                        # entering the guard_left list of values
            if i == "0":                            # if function for drawing
                self.drawing_white_line_long()          # calling the function drawing_whiteline_long when the number is zero
            else:
                self.drawing_blackline_long()           # calling the function drawing_blackline_long when the number is one

        # writing barcode
        self.tess.goto(-260, -100)              # setting position to write the barcode at the end
        self.tess.pensize(20)                   # setting the pen size

        upc_barcode_string = ""                 # starting an empty string to convert barcode list to barcode
        for i in self.upc_barcode:              # for each element in the barcode list
            upc_barcode_string += str(i)        # adding the values to the string.
        self.tess.write(upc_barcode_string[0] + "   "+upc_barcode_string[1:6] + "     "+upc_barcode_string[6:11] + "      " +upc_barcode_string[11], move=False, align="left", font=("Arial", 15, "normal"))    # writing the barcod
        self.tess.goto(-260, -150)              # setting position to write the barcode at the end
        self.tess.pencolor("dark blue")         # changing pen color to dark blue
        self.tess.write("Click on the screen if you want to access the product", move=False, align="left", font=("Arial", 15, "normal"))    # writing the barcod
        return upc_barcode_string

