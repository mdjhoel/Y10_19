'''
guess.py - program illustrating the basics of the Python language (using correct naming convention)

- sequential code, one line runs after the other logically to solve problem
- data types: boolean, integer, string
- data type casting: string to an int, int to a string
- variable storage in RAM and retreival
- user input from screen
- user output to screen
- selection or program flow control using if and else
- nested if statement, if something is true, do another test before taking an action
- while loop repetition, keep doing something while a condition is true

'''

# initialize variables
youguess = False
numtries = 0

# start loop, run until youguess is correct
while youguess == False:
    # all code is indented to denote that it is nested inside the loop
    numtries = numtries + 1 # increment number of tries
    correct = 974 # set correct number
    print("Guess a number between 1-100") # output to screen
    guess = input("Example: 200: ") # user input from screen - always returns string data

    numguess = int(guess) # convert string user guess to an int for use in if statement
    if (numguess == correct): # testing equality uses two equal signs
        str_tries =  str(numtries) # convert integer numtries to a string for use in output
        print("Well done!")
        print("You have solved the problem in " + str_tries + " tries.") # strings can be concatenated together
        youguess = True # end the loop
    else:
        if (numguess > correct): # nested if statement to give user information
            print("Wrong! Too high.")
        else:
            print("Wrong! Too low.")
        
