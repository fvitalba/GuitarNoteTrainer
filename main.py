from random import randint
import os
import fretboard_interpreter

# Main function
trainer_active = True
while trainer_active:
    print("Welcome to the Python Guitar Note Trainer.")
    print("")

    # Define a random position on the guitar neck
    guitar_string = randint(1,6)
    guitar_fret = randint(0,12)

    # In case we did not define a position, we simply print an additional message to prompt the user for the guitar string's name
    if guitar_fret == 0:
        print("What's the name for the string no. {} (from the top!)".format(guitar_string))

    # Print the fretboard with the note to guess
    position_array = fretboard_interpreter.create_single_position_array(guitar_string, guitar_fret)
    fretboard_interpreter.draw_fretboard(position_array, True, (guitar_fret != 0))
    fretboard_interpreter.draw_guitar_dots()

    print("")
    user_guess = input("What do you think this Note is (or type a command): ").upper()

    if (user_guess == "Q") or (user_guess == "QUIT"):
        # Quit the Trainer
        trainer_active = False

    elif (user_guess == "H") or (user_guess == "HELP"):
        # Print all the Notes present on the fretboard
        print("Here you can look at the fretboard again:")
        position_array = fretboard_interpreter.create_help_position_array()
        fretboard_interpreter.draw_fretboard(position_array, False, True)
        fretboard_interpreter.draw_guitar_dots()

    elif (user_guess == "S") or (user_guess == "SOLVE"):
        # Solve the current problem and print the fretboard including the solution
        print("This was the correct answer:")
        fretboard_interpreter.draw_fretboard(position_array, False, True)
        fretboard_interpreter.draw_guitar_dots()

    else:
        # No command was selected, we can compare the input
        starting_note = fretboard_interpreter.get_guitar_note_from_int(guitar_string)
        solution = fretboard_interpreter.get_correct_guitar_note(starting_note, guitar_fret)
        solution = solution[:2]

        # Convert both Solutions (user and system generated) and compare them
        if fretboard_interpreter.convert_note_to_number(user_guess) == fretboard_interpreter.convert_note_to_number(solution):
            print("Correct! Rock on!")
        else:
            # In case of a wrong guess, we print the correct note in the correct position
            print("Wrong! The correct answer was: {}".format(solution))
            fretboard_interpreter.draw_fretboard(position_array, False, True)
            fretboard_interpreter.draw_guitar_dots()

    #Avoid clearing screen immediately
    input()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
