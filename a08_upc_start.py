######################################################################
# Author: Dr. Scott Heggen       Emely Alfaro, Elaheh Jamali
# Username: heggens              alfarozavalae, jamalie
#
# Assignment: A08: UPC Barcodes
#
# Purpose: Determine how to do some basic operations on lists
#
######################################################################
# Acknowledgements:
#
# None: Original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import turtle                       # importing the turtle library


def is_valid_input(barcode):
    """
    This function verifies if the barcode is 12 digits and if they are all positive numbers.
    :param barcode:  parameter that takes the user's input to check if it is a valid 12 digit or not
    :return: Fruitful. a True or False Boolean value.
    """
    if len(barcode) == 12 and barcode.isnumeric():     # checks the user's input to see if it is a valid 12 digit barcode
        return True                 # true when the barcode is 12 digits

    return False                # returns false when it is not 12 digits input


def is_valid_modulo(barcode):
    """

    :param barcode: takes the user's input and does several operations to the odd and even positions with the module check character method.
    :return: checkdigit (the variable that should match the last digit of the barcode
    """
    oddnumbers = []                             # creating new list
    for i in range(0,len(barcode),2):           # creating for loop to go through the elements in the barcode starting from the first one (odd) and skipping every other one
        oddnumbers.append(barcode[i])           # appending into the oddnumbers list each of the elements retrieved in the for loop
    oddnumber_sum = sum(map(int,oddnumbers))    # adding all the elements in the list created and using map to make them integers
    oddbythree = int(oddnumber_sum) * 3         # multiplying the oddnumber_sum by three as one of the steps in module check character

    evennumbers = []                            # creates new empty list for even numbers
    for i in range(1,len(barcode),2):           # for loop to start in the first even element of the barcode and skipping every other one
        evennumbers.append(barcode[i])          # appending the retrieved even numbers into the empty list
    evennumbers = evennumbers[:-1]              # taking out the last even number (module check character)
    evennumber_sum = sum(map(int,evennumbers))  # adding all the even numbers after changing them into integers.
    final = oddbythree + evennumber_sum         # adding the result from odd numbers and even numbers to get to the final step
    final = final % 10                          # checking if the final number is divisible by 10 with modulus
    if final is not 0:                          # if function to check if the final digit is not zero
        checkdigit = 10 - final                 # subtracting 10 from the final one when the final is not zero
    else:
        checkdigit = final     # if there's no remainder in modulus of final % 10 the final value stays the same
    return checkdigit                           # returning the checkdigit value


def translate(barcode):
    """
    This function will translate the barcode into binary numbers so that we can draw the turtle by using the turtle module
    :param barcode: taking the barcode from the user's input
    :return: Fruitful. returns leftl and rights values of the lists lefside and rightside
    """
    leftside = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']  # creating a list with all the elements from the left side table.
    rightside = ['1110010','1100110','1101100','1000010','1011100','1001110','1010000','1000100','1001000','1110100']          # # creating a list with all the elements from the right side table.
    barcode = list(barcode)                     # making the barcode a list
    leftl = []                                  # creating an empty list to go through the first 6 elements of barcode
    for i in barcode[0:6]:                      # for loop to run in the first 6 elements
        lf = leftside[int(i)]                   # getting the first six elements of the list
        leftl.append(lf)                        # appending the first 6 elements into the leftl variable

    rights = []                                 # creating an empty list to go through the remainder 6 elements of barcode
    for i in barcode[6:12]:                     # for loop to run in the remainder 6 elements
        rs = rightside[int(i)]                  # getting the first six elements of the list
        rights.append(rs)                       # appending the first 6 elements into the leftl variable
    return (leftl, rights)                        # returning both leftl and rights to use them in main for drawing


def drawing_blackline(t):
    """

    :param t: turtle object that will draw the black lines in the barcode
    :return: None. Void
    """
    t.color("black")                            # setting the color of the turtle to be black
    t.begin_fill()                              # beginning to fill with the turtle
    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(200)                          # turtle t goes forward 200 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace


def drawing_blackline_long(t):
    """

    :param t: turtle object that will draw the black lines in the barcode for guard and center
    :return: None. Void
    """
    t.color("black")                            # setting the color of the turtle to be black
    t.begin_fill()

    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(248)                          # turtle t goes forward 248 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace


def drawing_white_line(t):
    """

    :param t: turtle object t to draw the while lines.
    :return: none. Void function .
    """
    t.color("white")                            # setting the color of the turtle to be black
    t.begin_fill()                              # beginning to fill with the turtle
    for i in range(2):                          # for loop to run twice
        t.forward(2)                            # turtle t moves forward by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(200)                          # turtle t goes forward 200 up
        t.left(90)                              # turtle t turns 90 degrees left again
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace


def drawing_white_line_long(t):
    """

    :param t: turtle object t to draw the while lines for guard and center
    :return: none. Void function .
    """
    t.color("white")                            # setting the color of the turtle to be black
    t.begin_fill()
    for i in range(2):                          # for loop to run twice
        t.forward(2)                                # moving to the right by 2
        t.left(90)                              # turtle t turns 90 degrees left to go up
        t.forward(248)                          # turtle t goes forward 248 up
        t.left(90)
    t.end_fill()                                # finishing the filling of t
    t.forward(2)                                # moving to the right by 2 without leaving a trace


def main():
    """

    :return: main function where the user is asked for a barcode and list is created to run the other functions that check characters in barcode
    """
    input_code = input("Enter a 12 digit code [0-9]: ")                         # asking user for input of barcode
    while not is_valid_input(input_code):                                       # while loop to check if it is valid
        input_code = input("Invalid number. Enter a 12 digit code [0-9]: ")    # asking user to input a valid barcode again
    list(input_code)  # making the barcode a list

    # TODO turtle draw code
    t = turtle.Turtle()                         # creating the turtle
    t.hideturtle()                              # hiding turtle to move its position
    wn = turtle.Screen()                        # creating the turtle screen
    t.speed(0)                                  # setting the speed of the turtle
    t.penup()                                   # putting the pen up to start moving
    t.setpos(-250, -100)                        # setting the left side position
    left, right = translate(input_code)         # calling the two return variables from the translate function

    if is_valid_modulo(input_code) != int(input_code[11]):       # if function run the module check character in the barcode
        t.write("Wrong barcode.", move=False, align="left", font=("Arial", 15, "normal"))       # writing the text when the barcode doesnt exist

    else:
        guard_left = ["1", "0", "1"]                # creating list for left guard
        for i in guard_left:                        # loop for left guard
            if i == "0":                            # if function for drawing white lines when i is 0
                drawing_white_line_long(t)
        else:
            drawing_blackline_long(t)               # # if function for drawing white lines when i is 0

        t.setpos(-244, -52)                         # setting the position

        for i in range(len(left)):                  # for loop to run in the len of the first 6 elements retrieved for the left side
            for j in left[i]:                       # nested for loop to run in the first 6-digit binary element inside the left side list
                if j == "0":                        # if the element is zero then
                    drawing_white_line(t)           # a white line is drawn
                else:
                    drawing_blackline(t)            # if it is anything else a black line is drawn
        t.setpos(-160, -100)                        # setting the position

    # center
        guard_center = ["0", "1", "0", "1", "0"]        # creating list for center guard
        for i in guard_center:                          # loop for center guard
            if i == "0":                                 # if function for drawing white lines when i is 0
                drawing_white_line_long(t)
            else:
                drawing_blackline_long(t)           # drawing black lines when i is not 0
        t.setpos(-150, -52)                         # setting the position
        for i in range(len(right)):                 # for loop # for loop to run in the len of the first 6 elements retrieved for the center side
            for j in right[i]:                      # nested for loop to run in the first 6-digit binary element inside the center side list
                print(j)                            # if the element is zero then
                if j == "0":                        # if the element is zero then
                    drawing_white_line(t)           # a white line is drawn
                else:
                    drawing_blackline(t)            # if it is anything else a black line is drawn
        t.setpos(-66, -100)                         # setting the position
    # right guard
        guard_left = ["1", "0", "1"]                # creating the list for the left guard
        for i in guard_left:                        # entering the guard_left list of values
            if i == "0":                            # if function for drawing
                drawing_white_line_long(t)          # calling the function drawing_whiteline_long when the number is zero
            else:
                drawing_blackline_long(t)           # calling the function drawing_blackline_long when the number is one

        # writing barcode
        t.goto(-260, -100)              # setting position to write the barcode at the end
        t.pensize(20)                   # setting the pen size
        t.write(input_code[0]+ "    "+input_code[1:6]+ "     "+input_code[6:11]+"     "+input_code[11], move=False, align="left", font=("Arial", 15, "normal"))    #writing the barcode and spaces in between

    wn.exitonclick()                        # exiting turtle drawing on click


if __name__ == "__main__":
    main()
