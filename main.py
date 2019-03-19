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
        "B#": 3,
        "C": 3,
        "C#": 4,
        "DM": 4,
        "D": 5,
        "D#": 6,
        "EM": 6,
        "E": 7,
        "E#": 8,
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
    return {
        1: "E",
        2: "A",
        3: "D",
        4: "G",
        5: "B",
        6: "E",
    }.get(string_no, "Invalid String No.")

def draw_fretboard(string_no, fret_no):
    # Creates a list containing 5 lists, each of 8 items, all set to 0
    strings, frets = 6, 12;
    str_pos = [["-" for x in range(frets)] for y in range(strings)]
    str_pos[string_no - 1][fret_no] = "X"

    # E
    print("{}  |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
    get_guitar_note_from_int(1),
    str_pos[0][0],str_pos[0][1],str_pos[0][2],str_pos[0][3],str_pos[0][4],str_pos[0][5],str_pos[0][6],str_pos[0][7],str_pos[0][8],str_pos[0][9],str_pos[0][10],str_pos[0][11]
    ))
    # A
    print("{}  |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
    get_guitar_note_from_int(2),
    str_pos[1][0],str_pos[1][1],str_pos[1][2],str_pos[1][3],str_pos[1][4],str_pos[1][5],str_pos[1][6],str_pos[1][7],str_pos[1][8],str_pos[1][9],str_pos[1][10],str_pos[1][11]
    ))
    # D
    print("{}  |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
    get_guitar_note_from_int(3),
    str_pos[2][0],str_pos[2][1],str_pos[2][2],str_pos[2][3],str_pos[2][4],str_pos[2][5],str_pos[2][6],str_pos[2][7],str_pos[2][8],str_pos[2][9],str_pos[2][10],str_pos[2][11]
    ))
    # G
    print("{}  |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
    get_guitar_note_from_int(4),
    str_pos[3][0],str_pos[3][1],str_pos[3][2],str_pos[3][3],str_pos[3][4],str_pos[3][5],str_pos[3][6],str_pos[3][7],str_pos[3][8],str_pos[3][9],str_pos[3][10],str_pos[3][11]
    ))
    # B
    print("{}  |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
    get_guitar_note_from_int(5),
    str_pos[4][0],str_pos[4][1],str_pos[4][2],str_pos[4][3],str_pos[4][4],str_pos[4][5],str_pos[4][6],str_pos[4][7],str_pos[4][8],str_pos[4][9],str_pos[4][10],str_pos[4][11]
    ))
    # E
    print("{}  |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
    get_guitar_note_from_int(6),
    str_pos[5][0],str_pos[5][1],str_pos[5][2],str_pos[5][3],str_pos[5][4],str_pos[5][5],str_pos[5][6],str_pos[5][7],str_pos[5][8],str_pos[5][9],str_pos[5][10],str_pos[5][11]
    ))

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
