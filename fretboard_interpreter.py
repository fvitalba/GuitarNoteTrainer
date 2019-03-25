import guitar_constant

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

# Italian / International Notes?
# Do=C Re=D Mi=E Fa=F So=G La=A Ti=B

# This function converts the Note to a Number, increments it and returns the correct note
def get_correct_guitar_note(starting_note, increment):
    int_note = convert_note_to_number(starting_note)
    
    act_increment = increment % 12
    int_note += act_increment
    int_note = int_note % 12

    ending_note = convert_number_to_note(int_note)

    return ending_note;

# Convert a text (note) to a number
def convert_note_to_number(note):
    note = note.upper()
    return {
        "A": 0,
        "A#": 1,
        "BB": 1,
        "B": 2,
        "B#": 3,
        "C": 3,
        "C#": 4,
        "DB": 4,
        "D": 5,
        "D#": 6,
        "EB": 6,
        "E": 7,
        "E#": 8,
        "F": 8,
        "F#": 9,
        "GB": 9,
        "G": 10,
        "G#": 11,
        "AB": 11,
    }.get(note, -1)

# Convert an integer to a text (note)
def convert_number_to_note(int_note):
    return {
        0 : "A",
        1 : "A# / Bb",
        2 : "B",
        3 : "C",
        4 : "C# / Db",
        5 : "D",
        6 : "D# / Eb",
        7 : "E",
        8 : "F",
        9 : "F# / Gb",
        10: "G",
        11: "G# / Ab",
    }.get(int_note, "Invalid Note")

# Get the Guitar String Name from an integer
def get_guitar_note_from_int(string_no):
    return {
        6: "E",
        5: "A",
        4: "D",
        3: "G",
        2: "B",
        1: "e",
    }.get(string_no, "Invalid String No.")

# Dynamically draw a fretboard, filling in the needed characters based on the position_array (boolean) and the hidden (boolean) property
def draw_fretboard(position_array, hidden, show_string_name):
    for si in range(guitar_constant.GUITAR_STRINGS):
        if show_string_name:
            guitar_string = get_guitar_note_from_int(si + 1).ljust(4, " ")
        else:
            guitar_string = "".ljust(4, " ")
        guitar_string += guitar_constant.FRETBOARD_SEPERATOR
        for fi in range(1, guitar_constant.GUITAR_FRETS + 1):
            if position_array[si][fi]:
                if hidden:
                    guitar_string += guitar_constant.FINGER_CHARACTER.center(guitar_constant.FRETSPACE, guitar_constant.FILLER_CHARACTER)
                else:
                    guitar_string += get_correct_guitar_note(
                            get_guitar_note_from_int(si + 1),fi
                        ).center(guitar_constant.FRETSPACE," ")
            else:
                guitar_string += guitar_constant.FILLER_CHARACTER.center(guitar_constant.FRETSPACE, guitar_constant.FILLER_CHARACTER)
            guitar_string += guitar_constant.FRETBOARD_SEPERATOR
        print(guitar_string)

# Draw the guitars dots for each needed fretboard
def draw_guitar_dots():
    dot_string = "".ljust(4)
    for fi in range(guitar_constant.GUITAR_FRETS + 1):
        dot_string += " "
        if fi in [11, 23]:
            # Double Dot
            dot_string += "{} {}".format(
                    guitar_constant.GUITAR_DOT_CHARACTER, guitar_constant.GUITAR_DOT_CHARACTER
                ).center(guitar_constant.FRETSPACE, " ")
        elif fi in [2, 4, 6, 8, 14, 16, 18, 20]:
            # Single Dot
            dot_string += guitar_constant.GUITAR_DOT_CHARACTER.center(guitar_constant.FRETSPACE, " ")
        else:
            # Empty Fret
            dot_string += " ".center(guitar_constant.FRETSPACE, " ")
    print(dot_string)

# Create a position array from a single position
def create_single_position_array(string_no, fret_no):
    position_array = [[False for x in range(guitar_constant.GUITAR_FRETS + 1)] for y in range(guitar_constant.GUITAR_STRINGS)]
    position_array[string_no - 1][fret_no] = True
    return position_array

# Create a position array for a help
def create_help_position_array():
    position_array = [[True for x in range(guitar_constant.GUITAR_FRETS + 1)] for y in range(guitar_constant.GUITAR_STRINGS)]
    return position_array
