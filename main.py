from random import randint

# this function converts the Note to a Number, increments it and returns the correct note
def get_correct_guitar_note(starting_note, increment):
    int_note = convert_note_to_number(starting_note)
    # DEBUG:
    #print("note: {} --> Number {}".format(starting_note,int_note))
    act_increment = increment % 12
    # DEBUG:
    #print("act_increment: {}".format(act_increment))
    int_note += act_increment
    int_note = int_note % 12

    ending_note = convert_number_to_note(int_note)
    # DEBUG:
    #print("int_note: {} --> note: {}".format(int_note,ending_note))

    return ending_note;

# Guitar Notes
# A
# A# / Bm
# B
# C
# C# / Dm
# D
# D# / Em
# E
# F
# F# / Gm
# G
# G# / Am

# Convert a text (note) to a number
def convert_note_to_number(note):
    return {
        "A": 0,
        "A#": 1,
        "BM": 1,
        "B": 2,
        "C": 3,
        "C#": 4,
        "DM": 4,
        "D": 5,
        "D#": 6,
        "EM": 6,
        "E": 7,
        "F": 8,
        "F#": 9,
        "GM": 9,
        "G": 10,
        "G#": 11,
        "AM": 11,
    }.get(note, -1)

# Convert an integer to a text (note)
def convert_number_to_note(int_note):
    return {
        0 : "A",
        1 : "A# / Bm",
        2 : "B",
        3 : "C",
        4 : "C# / Dm",
        5 : "D",
        6 : "D# / Em",
        7 : "E",
        8 : "F",
        9 : "F# / Gm",
        10: "G",
        11: "G# / Am",
    }.get(int_note, "Invalid Note")

# Get the Guitar String Name from an integer
def get_guitar_note_from_int(string_no):
    # Guitar Strings
    # E --> Lowest
    # A
    # D
    # G
    # B
    # E --> Highest
    return {
        1: "E",
        2: "A",
        3: "D",
        4: "G",
        5: "B",
        6: "E",
    }.get(string_no, "Invalid String No.")

def draw_fretboard(string_no, fret_no):


print("Welcome to the Python Guitar Note Trainer.")
print("")
print("")

trainer_active = True
while (trainer_active):
    # Define a random position on the guitar neck
    guitar_string = randint(1,6)
    guitar_fret = randint(0,12)
    print("Please try to convert the following constellation: Guitar String: {}, Guitar Fret: {}".format(guitar_string, guitar_fret))
    draw_fretboard(guitar_string,guitar_fret)
    print("")
    user_guess = input("What do you think this Note is: ")

    if (user_guess.upper() == "Q") or (user_guess.upper() == "QUIT"):
        trainer_active = False

    if trainer_active:
        starting_note = get_guitar_note_from_int(guitar_string)
        # DEBUG:
        #print("starting_note: {}".format(starting_note))
        correct_guess = get_correct_guitar_note(starting_note,guitar_fret)
        # DEBUG:
        #print("correct_guess: {}".format(correct_guess))
        correct_guess = correct_guess[:2]

        # DEBUG:
        #print("user_guess: {} {}".format(user_guess.upper(),convert_note_to_number(user_guess.upper())))
        #print("correct_guess: {} {}".format(correct_guess.upper(),convert_note_to_number(correct_guess.upper())))
        if (convert_note_to_number(user_guess.upper()) == convert_note_to_number(correct_guess.upper())):
            print("Correct!")
        else:
            print("Wrong! The correct answer was: {}".format(correct_guess))
