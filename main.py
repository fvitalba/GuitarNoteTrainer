from random import randint
import os
import fretboard_interpreter

# Main function
trainer_active = True
while (trainer_active):
    print("Welcome to the Python Guitar Note Trainer.")
    print("")
    print("")

    # Define a random position on the guitar neck
    guitar_string = randint(1,6)
    guitar_fret = randint(0,12)

    if (guitar_fret == 0):
        print("Please try to convert the following constellation: Guitar String: {}, Guitar Fret: {}".format(guitar_string, guitar_fret))

    position_array = fretboard_interpreter.create_single_position_array(guitar_string, guitar_fret)
    fretboard_interpreter.draw_fretboard(position_array, True)
    fretboard_interpreter.draw_guitar_dots()

    print("")
    user_guess = input("What do you think this Note is (or type a command): ")
    verify_note = True

    if (user_guess.upper() == "Q") or (user_guess.upper() == "QUIT"):
        trainer_active = False
    elif (user_guess.upper() == "H") or (user_guess.upper() == "HELP"):
        verify_note = False
        print("These are all the notes")
        #draw_fretboard_with_notes()
        position_array = fretboard_interpreter.create_help_position_array()
        fretboard_interpreter.draw_fretboard(position_array, False)
        fretboard_interpreter.draw_guitar_dots()

    if trainer_active:
        if verify_note:
            starting_note = fretboard_interpreter.get_guitar_note_from_int(guitar_string).upper()
            # DEBUG:
            #print("starting_note: {}".format(starting_note))
            correct_guess = fretboard_interpreter.get_correct_guitar_note(starting_note,guitar_fret)
            # DEBUG:
            #print("correct_guess: {}".format(correct_guess))
            correct_guess = correct_guess[:2]

            # DEBUG:
            #print("user_guess: {} {}".format(user_guess.upper(),convert_note_to_number(user_guess.upper())))
            #print("correct_guess: {} {}".format(correct_guess.upper(),convert_note_to_number(correct_guess.upper())))
            if (fretboard_interpreter.convert_note_to_number(user_guess.upper()) == fretboard_interpreter.convert_note_to_number(correct_guess.upper())):
                print("Correct!")
            else:
                print("Wrong! The correct answer was: {}".format(correct_guess))

        input() #Avoid clearing screen immediately
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
